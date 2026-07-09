from sqlalchemy.orm import Session

from app.models import Payment
from common.publisher import publish_event
from common.events import (
    PAYMENT_COMPLETED,
    REFUND_COMPLETED
)


class PaymentService:

    @staticmethod
    async def process_payment(
        db: Session,
        event: dict
    ):
        """
        Process payment for an order.
        """

        payment = Payment(
            order_id=event["order_id"],
            amount=event["amount"],
            status="SUCCESS"
        )

        db.add(payment)
        db.commit()
        db.refresh(payment)

        print(f"Payment Successful for Order {payment.order_id}")

        await publish_event(
            routing_key=PAYMENT_COMPLETED,
            payload={
                "order_id": payment.order_id
            }
        )

        print("Published -> payment.completed")

    @staticmethod
    async def refund_payment(
        db: Session,
        event: dict
    ):
        """
        Compensating transaction.
        Refund previously successful payment.
        """

        payment = (
            db.query(Payment)
            .filter(
                Payment.order_id == event["order_id"]
            )
            .first()
        )

        if payment is None:

            print("Payment not found")

            return

        payment.status = "REFUNDED"

        db.commit()

        print(f"Refund completed for Order {payment.order_id}")

        await publish_event(
            routing_key=REFUND_COMPLETED,
            payload={
                "order_id": payment.order_id
            }
        )

        print("Published -> refund.completed")