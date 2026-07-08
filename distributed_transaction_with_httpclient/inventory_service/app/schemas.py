from pydantic import BaseModel

from app.models import InventoryStatus


class InventoryRequest(BaseModel):

    order_id: int

    product_name: str

    quantity: int


class InventoryResponse(BaseModel):

    id: int

    order_id: int

    product_name: str

    quantity: int

    status: InventoryStatus

    class Config:
        from_attributes = True
