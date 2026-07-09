from sqlalchemy.orm import Session

from .models import Payment

from common.publisher import publish_event
from common.events import (
    PAYMENT_COMPLETED,
    PAYMENT_REFUNDED
)


class PaymentService:

    @staticmethod
    async def process_payment(
        db: Session,
        event: dict
    ):

        existing_payment = (
            db.query(Payment)
            .filter(
                Payment.order_id == event["order_id"]
            )
            .first()
        )

        if existing_payment:

            print(
                f"Payment already processed for Order {event['order_id']}"
            )

            return

        payment = Payment(

            order_id=event["order_id"],

            amount=event["amount"],

            status="SUCCESS"

        )

        db.add(payment)

        db.commit()

        db.refresh(payment)

        print(
            f"Payment Successful : {payment.order_id}"
        )

        await publish_event(

            routing_key=PAYMENT_COMPLETED,

            payload={

                "saga_id": event["saga_id"],

                "order_id": payment.order_id

            }

        )

        print(
            f"Saga : {event['saga_id']}"
        )

    @staticmethod
    async def refund_payment(
        db: Session,
        event: dict
    ):

        payment = (

            db.query(Payment)

            .filter(
                Payment.order_id == event["order_id"]
            )

            .first()

        )

        if payment is None:

            print("Payment Not Found")

            return
        
        if payment.status == "REFUNDED":

            print(
                "Already Refunded"
            )

            return

        payment.status = "REFUNDED"

        db.commit()

        print(
            f"Payment Refunded : {payment.order_id}"
        )

        await publish_event(

            routing_key=PAYMENT_REFUNDED,

            payload={

                "saga_id": event["saga_id"],

                "order_id": payment.order_id

            }

        )