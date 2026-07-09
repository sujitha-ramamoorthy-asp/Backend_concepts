from pydantic import BaseModel


class InventoryResponse(BaseModel):

    id: int

    order_id: int

    product: str

    quantity: int

    status: str

    class Config:

        from_attributes = True