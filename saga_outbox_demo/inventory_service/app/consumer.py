import json

from common.rabbitmq import get_channel

from inventory_service.app.database import SessionLocal

from inventory_service.app.service import InventoryService

from inventory_service.app.publisher import InventoryPublisher

channel = get_channel()


def callback(ch, method, properties, body):

    db = SessionLocal()

    data = json.loads(body)
    print("ggggggggggggggggg")
    success = InventoryService.reserve_inventory(
        db,
        data["product"],
        data["quantity"]
    )

    if success:

        InventoryPublisher.publish_reserved(
            data["order_id"]
        )

    else:

        InventoryPublisher.publish_failed(
            data["order_id"]
        )

    db.close()

    ch.basic_ack(
        delivery_tag=method.delivery_tag
    )


channel.basic_consume(
    queue="order_created",
    on_message_callback=callback
)

print("Inventory Consumer Started...")

channel.start_consuming()