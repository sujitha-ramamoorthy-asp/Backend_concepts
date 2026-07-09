import asyncio
import json

from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import PAYMENT_COMPLETED

from .database import SessionLocal
from .service import InventoryService


class InventoryConsumer:

    @staticmethod
    async def payment_completed(message):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("\n========================")
            print("Received : payment.completed")
            print("Saga ID  :", event["saga_id"])
            print("========================")

            db: Session = SessionLocal()

            try:

                await InventoryService.reserve_inventory(
                    db,
                    event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    queue = await channel.declare_queue(

        "inventory_payment_completed_queue",

        durable=True

    )

    await queue.bind(

        exchange,

        routing_key=PAYMENT_COMPLETED

    )

    await queue.consume(

        InventoryConsumer.payment_completed

    )

    print(
        "Inventory Consumer Started"
    )

    await asyncio.Future()