import asyncio
import json

import aio_pika
from sqlalchemy.orm import Session

from common.rabbitmq import get_channel
from common.events import (
    ORDER_CREATED,
    REFUND_REQUEST,
)

from app.database import SessionLocal
from app.service import PaymentService


class PaymentConsumer:

    @staticmethod
    async def order_created(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : order.created")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                await PaymentService.process_payment(
                    db=db,
                    event=event
                )

            finally:

                db.close()

    @staticmethod
    async def refund_request(message: aio_pika.IncomingMessage):

        async with message.process():

            event = json.loads(message.body.decode())

            print("\n===================================")
            print("Received : refund.request")
            print(event)
            print("===================================")

            db: Session = SessionLocal()

            try:

                await PaymentService.refund_payment(
                    db=db,
                    event=event
                )

            finally:

                db.close()


async def start_consumer():

    connection, channel, exchange = await get_channel()

    ####################################################
    # order.created
    ####################################################

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

    ####################################################
    # refund.request
    ####################################################

    refund_queue = await channel.declare_queue(
        "payment_refund_request_queue",
        durable=True
    )

    await refund_queue.bind(
        exchange,
        routing_key=REFUND_REQUEST
    )

    await refund_queue.consume(
        PaymentConsumer.refund_request
    )

    print("\n===================================")
    print("Payment Consumer Started")
    print("===================================")

    await asyncio.Future()