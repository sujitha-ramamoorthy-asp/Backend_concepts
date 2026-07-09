import time

from order_service.app.database import SessionLocal
from common.rabbitmq import get_channel

from order_service.app.models import Outbox

channel = get_channel()

print("Order Publisher Started...")

while True:

    db = SessionLocal()

    events = db.query(Outbox).filter(
        Outbox.published == False
    ).all()

    for event in events:

        channel.basic_publish(
            exchange="",
            routing_key="order_created",
            body=event.payload
        )

        print("Published :", event.payload)

        event.published = True

    db.commit()

    db.close()

    time.sleep(5)