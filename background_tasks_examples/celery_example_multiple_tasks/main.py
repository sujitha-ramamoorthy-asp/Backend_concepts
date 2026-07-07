from fastapi import FastAPI

from database import save_order
from tasks.email import send_order_email
from tasks.report import generate_order_report

app = FastAPI()


@app.post("/orders")
async def create_order():

    order = save_order(
        {
            "customer": "abc",
            "email": "def@gmail.com",
            "product": "Laptop",
            "quantity": 2,
            "price": 50000
        }
    )
    print("abc  ----------------- xyz")

    # Queue the email task
    send_order_email.delay(
        order["email"],
        order["id"]
    )
    generate_order_report.delay(order)

    return {
        "message": "Order Created Successfully",
        "order_id": order["id"]
    }