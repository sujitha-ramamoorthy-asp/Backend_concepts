import json

import aio_pika

from common.rabbitmq import get_channel


async def publish_event(
    routing_key: str,
    payload: dict
):

    connection, channel, exchange = await get_channel()

    async with connection:

        message = aio_pika.Message(

            body=json.dumps(payload).encode(),

            delivery_mode=aio_pika.DeliveryMode.PERSISTENT
        )

        await exchange.publish(

            message,

            routing_key=routing_key

        )

        print(
            f"Published -> {routing_key} : {payload}"
        )