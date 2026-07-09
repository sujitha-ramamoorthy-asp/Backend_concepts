import aio_pika

from common.config import RABBITMQ_URL


async def get_channel():

    connection = await aio_pika.connect_robust(
        RABBITMQ_URL
    )

    channel = await connection.channel()

    exchange = await channel.declare_exchange(
        "saga_exchange",
        aio_pika.ExchangeType.DIRECT,
        durable=True
    )

    return connection, channel, exchange