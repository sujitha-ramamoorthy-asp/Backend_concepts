from pydantic import BaseModel

from app.models import PaymentStatus


class PaymentRequest(BaseModel):

    order_id: int

    amount: float


class PaymentResponse(BaseModel):

    id: int

    order_id: int

    amount: float

    status: PaymentStatus

    class Config:

        from_attributes = True
