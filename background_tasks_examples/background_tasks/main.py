from fastapi import FastAPI, BackgroundTasks

from database import save_order
from services import send_order_email

app = FastAPI()


@app.post("/orders")
async def create_order(background_tasks: BackgroundTasks):

    order = save_order(
        {
            "customer": "abc",
            "email": "abc@gmail.com",
            "phone": "+911234567891",  
            "product": "Laptop"
        }
    )

    # Send email in the background
    background_tasks.add_task(
        send_order_email,
        order["email"],
        order["id"]
    )

    return {
        "message": "Order created successfully.",
        "order_id": order["id"]
    }