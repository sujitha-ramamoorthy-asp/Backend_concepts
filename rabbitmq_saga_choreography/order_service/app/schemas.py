from pydantic import BaseModel


class OrderRequest(BaseModel):

    customer: str

    amount: float


class OrderResponse(BaseModel):

    id: int

    customer: str

    amount: float

    status: str

    class Config:

        from_attributes = True