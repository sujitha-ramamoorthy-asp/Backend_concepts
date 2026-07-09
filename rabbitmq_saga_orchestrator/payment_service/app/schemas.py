from pydantic import BaseModel


class OrderCreatedEvent(BaseModel):

    order_id: int

    customer: str

    amount: float


class PaymentCompletedEvent(BaseModel):

    order_id: int

    status: str = "SUCCESS"