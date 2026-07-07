from fastapi import FastAPI

from database import save_order
from tasks import send_order_email

app = FastAPI()


@app.post("/orders")
async def create_order():

    order = save_order(
        {
            "customer": "abc",
            "email": "def@gmail.com",
            "product": "Laptop"
        }
    )

    # Queue the email task
    send_order_email.delay(
        order["email"],
        order["id"]
    )

    return {
        "message": "Order Created Successfully",
        "order_id": order["id"]
    }