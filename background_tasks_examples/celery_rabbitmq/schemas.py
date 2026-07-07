from pydantic import BaseModel

class OrderCreate(BaseModel):

    customer_name: str

    customer_email: str

    product_name: str

    quantity: int