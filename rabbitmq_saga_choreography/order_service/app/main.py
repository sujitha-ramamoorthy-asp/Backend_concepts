import asyncio

from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import (
    Base,
    engine,
    SessionLocal
)

from .schemas import (
    OrderRequest,
    OrderResponse
)

from .service import OrderService
from .consumer import start_consumer


Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()


@asynccontextmanager
async def lifespan(app: FastAPI):

    asyncio.create_task(
        start_consumer()
    )

    yield


app = FastAPI(
    title="Order Service",
    lifespan=lifespan
)


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


@app.get("/")
async def home():

    return {
        "message": "Order Service Running"
    }