from pydantic import BaseModel


class PaymentResponse(BaseModel):

    id: int

    order_id: int

    amount: float

    status: str

    class Config:

        from_attributes = True