import json

from common.rabbitmq import get_channel

channel = get_channel()


class InventoryPublisher:

    @staticmethod
    def publish_reserved(order_id):

        payload = json.dumps({
            "order_id": order_id
        })

        channel.basic_publish(
            exchange="",
            routing_key="inventory_reserved",
            body=payload
        )

        print("Published Inventory Reserved")


    @staticmethod
    def publish_failed(order_id):

        payload = json.dumps({
            "order_id": order_id
        })

        channel.basic_publish(
            exchange="",
            routing_key="inventory_failed",
            body=payload
        )

        print("Published Inventory Failed")