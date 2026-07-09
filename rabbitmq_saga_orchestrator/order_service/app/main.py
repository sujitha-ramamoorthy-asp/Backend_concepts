from contextlib import asynccontextmanager

import asyncio
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.schemas import OrderRequest, OrderResponse
from app.service import OrderService
from app.consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Runs once when the application starts.
    """

    # Create database tables
    Base.metadata.create_all(bind=engine)

    # Start RabbitMQ consumer in the background
    consumer_task = asyncio.create_task(start_consumer())

    print("===================================")
    print("Order Service Started")
    print("RabbitMQ Consumer Started")
    print("===================================")

    yield

    print("Stopping Order Service...")

    consumer_task.cancel()

    try:
        await consumer_task
    except asyncio.CancelledError:
        print("RabbitMQ Consumer Stopped")


app = FastAPI(
    title="Order Service",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
async def home():
    return {
        "message": "Order Service is Running"
    }


@app.post(
    "/orders",
    response_model=OrderResponse
)
async def create_order(
    request: OrderRequest,
    db: Session = Depends(get_db)
):
    return await OrderService.create_order(
        db=db,
        request=request
    )