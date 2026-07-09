import json

from common.rabbitmq import get_channel
from order_service.app.database import SessionLocal

from order_service.app.models import Order

channel = get_channel()


def callback(ch, method, properties, body):

    db = SessionLocal()

    data = json.loads(body)
    print(data["order_id"])

    order = db.query(Order).filter(
        Order.id == data["order_id"]
    ).first()

    if method.routing_key == "inventory_reserved":

        order.status = "CONFIRMED"

        print("Inventory Reserved")

    elif method.routing_key == "inventory_failed":

        order.status = "CANCELLED"

        print("Inventory Failed")

    db.commit()

    db.close()

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_consume(
    queue="inventory_reserved",
    on_message_callback=callback
)

channel.basic_consume(
    queue="inventory_failed",
    on_message_callback=callback
)

print("Order Consumer Started...")

channel.start_consuming()