from pydantic import BaseModel


class OrderRequest(BaseModel):

    product: str

    quantity: int