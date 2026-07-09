import asyncio
import json

import aio_pika
from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import (
    PAYMENT_COMPLETED,
    INVENTORY_COMPLETED,
    INVENTORY_FAILED,
    REFUND_COMPLETED,
)

from app.database import SessionLocal
from app.service import OrderService


class OrderConsumer:

    @staticmethod
    async def payment_completed(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : payment.completed")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                await OrderService.handle_payment_completed(
                    db=db,
                    event=event
                )

            finally:

                db.close()

    @staticmethod
    async def inventory_completed(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : inventory.completed")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                OrderService.handle_inventory_completed(
                    db=db,
                    event=event
                )

            finally:

                db.close()

    @staticmethod
    async def inventory_failed(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : inventory.failed")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                await OrderService.handle_inventory_failed(
                    db=db,
                    event=event
                )

            finally:

                db.close()

    @staticmethod
    async def refund_completed(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : refund.completed")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                OrderService.handle_refund_completed(
                    db=db,
                    event=event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    ####################################################
    # payment.completed
    ####################################################

    payment_queue = await channel.declare_queue(
        "order_payment_completed_queue",
        durable=True
    )

    await payment_queue.bind(
        exchange,
        routing_key=PAYMENT_COMPLETED
    )

    await payment_queue.consume(
        OrderConsumer.payment_completed
    )

    ####################################################
    # inventory.completed
    ####################################################

    inventory_completed_queue = await channel.declare_queue(
        "order_inventory_completed_queue",
        durable=True
    )

    await inventory_completed_queue.bind(
        exchange,
        routing_key=INVENTORY_COMPLETED
    )

    await inventory_completed_queue.consume(
        OrderConsumer.inventory_completed
    )

    ####################################################
    # inventory.failed
    ####################################################

    inventory_failed_queue = await channel.declare_queue(
        "order_inventory_failed_queue",
        durable=True
    )

    await inventory_failed_queue.bind(
        exchange,
        routing_key=INVENTORY_FAILED
    )

    await inventory_failed_queue.consume(
        OrderConsumer.inventory_failed
    )

    ####################################################
    # refund.completed
    ####################################################

    refund_completed_queue = await channel.declare_queue(
        "order_refund_completed_queue",
        durable=True
    )

    await refund_completed_queue.bind(
        exchange,
        routing_key=REFUND_COMPLETED
    )

    await refund_completed_queue.consume(
        OrderConsumer.refund_completed
    )

    print("\n===================================")
    print("Order Saga Consumer Started")
    print("===================================")

    # Keep consumer running
    await asyncio.Future()