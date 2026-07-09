import asyncio
import json

import aio_pika
from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import (
    INVENTORY_COMPLETED,
    PAYMENT_REFUNDED
)

from .database import SessionLocal
from .service import OrderService


class OrderConsumer:

    @staticmethod
    async def inventory_completed(
        message: aio_pika.IncomingMessage
    ):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("\n================================")
            print("EVENT RECEIVED")
            print("================================")
            print("Event    : inventory.completed")
            print("Saga ID  :", event["saga_id"])
            print("Order ID :", event["order_id"])

            db: Session = SessionLocal()

            try:

                OrderService.inventory_completed(
                    db=db,
                    event=event
                )

            finally:

                db.close()

    @staticmethod
    async def payment_refunded(
        message: aio_pika.IncomingMessage
    ):

        async with message.process():

            event = json.loads(
                message.body.decode()
            )

            print("\n================================")
            print("EVENT RECEIVED")
            print("================================")
            print("Event    : payment.refunded")
            print("Saga ID  :", event["saga_id"])
            print("Order ID :", event["order_id"])

            db: Session = SessionLocal()

            try:

                OrderService.payment_refunded(
                    db=db,
                    event=event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    ##################################################
    # inventory.completed
    ##################################################

    inventory_queue = await channel.declare_queue(

        "order_inventory_completed_queue",

        durable=True

    )

    await inventory_queue.bind(

        exchange,

        routing_key=INVENTORY_COMPLETED

    )

    await inventory_queue.consume(

        OrderConsumer.inventory_completed

    )

    ##################################################
    # payment.refunded
    ##################################################

    refund_queue = await channel.declare_queue(

        "order_payment_refunded_queue",

        durable=True

    )

    await refund_queue.bind(

        exchange,

        routing_key=PAYMENT_REFUNDED

    )

    await refund_queue.consume(

        OrderConsumer.payment_refunded

    )

    print("\n================================")
    print("Order Consumer Started")
    print("================================")
    print("Listening for:")
    print("- inventory.completed")
    print("- payment.refunded")

    await asyncio.Future()