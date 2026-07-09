import asyncio
import json

import aio_pika
from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import (
    INVENTORY_RESERVE,
)

from app.database import SessionLocal
from app.service import InventoryService


class InventoryConsumer:

    @staticmethod
    async def inventory_reserve(
        message: aio_pika.IncomingMessage
    ):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("\n===================================")
            print("Received : inventory.reserve")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                await InventoryService.reserve_inventory(
                    db=db,
                    event=event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    queue = await channel.declare_queue(

        "inventory_reserve_queue",

        durable=True

    )

    await queue.bind(

        exchange,

        routing_key=INVENTORY_RESERVE

    )

    await queue.consume(

        InventoryConsumer.inventory_reserve

    )

    print("\n===================================")
    print("Inventory Consumer Started")
    print("===================================")

    await asyncio.Future()