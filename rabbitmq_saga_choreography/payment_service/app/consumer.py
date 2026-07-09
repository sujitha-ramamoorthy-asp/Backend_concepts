import asyncio
import json

import aio_pika
from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import (
    ORDER_CREATED,
    INVENTORY_FAILED
)

from .database import SessionLocal
from .service import PaymentService


class PaymentConsumer:

    @staticmethod
    async def order_created(message):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("\n========================")
            print("Received : order.completed")
            print("Saga ID  :", event["saga_id"])
            print("========================")

            db: Session = SessionLocal()

            try:

                await PaymentService.process_payment(
                    db,
                    event
                )

            finally:

                db.close()

    @staticmethod
    async def inventory_failed(message):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("Received : inventory.failed")

            db: Session = SessionLocal()

            try:

                await PaymentService.refund_payment(
                    db,
                    event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    order_queue = await channel.declare_queue(
        "payment_order_created_queue",
        durable=True
    )

    await order_queue.bind(
        exchange,
        routing_key=ORDER_CREATED
    )

    await order_queue.consume(
        PaymentConsumer.order_created
    )

    inventory_queue = await channel.declare_queue(
        "payment_inventory_failed_queue",
        durable=True
    )

    await inventory_queue.bind(
        exchange,
        routing_key=INVENTORY_FAILED
    )

    await inventory_queue.consume(
        PaymentConsumer.inventory_failed
    )

    print("Payment Consumer Started")

    await asyncio.Future()