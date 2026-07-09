from pydantic import BaseModel


class InventoryReserveEvent(BaseModel):

    order_id: int


class InventoryCompletedEvent(BaseModel):

    order_id: int
    status: str = "RESERVED"