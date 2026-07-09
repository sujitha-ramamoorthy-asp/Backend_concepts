import json

import aio_pika

from .rabbitmq import get_channel


async def publish_event(
    routing_key: str,
    payload: dict
):

    connection, channel, exchange = await get_channel()

    try:

        message = aio_pika.Message(

            body=json.dumps(payload).encode(),

            delivery_mode=aio_pika.DeliveryMode.PERSISTENT

        )

        await exchange.publish(
            message,
            routing_key=routing_key
        )

        print("\n==============================")
        print("EVENT PUBLISHED")
        print("==============================")
        print("Routing Key :", routing_key)
        print("Saga ID     :", payload.get("saga_id"))
        print("Payload     :", payload)

    finally:

        await connection.close()