import aio_pika

from .config import (
    RABBITMQ_URL,
    EXCHANGE_NAME
)


async def get_channel():

    connection = await aio_pika.connect_robust(
        RABBITMQ_URL
    )

    channel = await connection.channel()

    exchange = await channel.declare_exchange(
        EXCHANGE_NAME,
        aio_pika.ExchangeType.TOPIC,
        durable=True
    )

    return connection, channel, exchange