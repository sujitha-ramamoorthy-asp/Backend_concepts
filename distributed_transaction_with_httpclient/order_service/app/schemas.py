from pydantic import BaseModel
from app.models import OrderStatus


class OrderCreate(BaseModel):

    customer_name: str

    product_name: str

    quantity: int

    amount: float


class OrderResponse(BaseModel):

    id: int

    customer_name: str

    product_name: str

    quantity: int

    amount: float

    status: OrderStatus

    class Config:
        from_attributes = True