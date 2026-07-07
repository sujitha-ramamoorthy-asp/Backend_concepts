import os
from datetime import datetime

from celery_app import celery


@celery.task
def generate_order_report(order: dict):

    # Create reports directory if it doesn't exist
    os.makedirs("reports", exist_ok=True)

    filename = f"reports/order_{order['id']}.txt"

    with open(filename, "w") as file:

        file.write("ABC STORE\n")
        file.write("=" * 40 + "\n")
        file.write(f"Generated On : {datetime.now()}\n\n")

        file.write(f"Order ID     : {order['id']}\n")
        file.write(f"Customer     : {order['customer']}\n")
        file.write(f"Email        : {order['email']}\n")
        file.write(f"Product      : {order['product']}\n")
        file.write(f"Quantity     : {order['quantity']}\n")
        file.write(f"Price        : ${order['price']}\n")
        file.write(f"Total Amount : ${order['quantity'] * order['price']}\n")