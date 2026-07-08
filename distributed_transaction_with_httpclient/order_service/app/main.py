from contextlib import asynccontextmanager
from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app.schemas import OrderCreate
from app.schemas import OrderResponse

from app.models import OrderStatus

from app.service import OrderService
from app.http_client import client


# Create all tables when the application starts

@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    yield

    await client.aclose()

app = FastAPI(
    title="Order Service",
    version="1.0.0",
    lifespan=lifespan
)


@app.get("/")
def home():
    return {
        "service": "Order Service",
        "status": "Running"
    }


@app.post(
    "/orders",
    response_model=OrderResponse,
    status_code=201
)
async def create_order(
    request: OrderCreate,
    db: Session = Depends(get_db)
):

    return await OrderService.create_order(
        db,
        request
    )


@app.get(
    "/orders",
    response_model=list[OrderResponse]
)
def get_orders(
    db: Session = Depends(get_db)
):
    return OrderService.get_all_orders(db)


@app.get(
    "/orders/{order_id}",
    response_model=OrderResponse
)
def get_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = OrderService.get_order(
        db,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@app.put(
    "/orders/{order_id}/complete",
    response_model=OrderResponse
)
def complete_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = OrderService.update_status(
        db,
        order_id,
        OrderStatus.COMPLETED
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order


@app.put(
    "/orders/{order_id}/cancel",
    response_model=OrderResponse
)
def cancel_order(
    order_id: int,
    db: Session = Depends(get_db)
):

    order = OrderService.cancel_order(
        db,
        order_id
    )

    if not order:
        raise HTTPException(
            status_code=404,
            detail="Order not found"
        )

    return order