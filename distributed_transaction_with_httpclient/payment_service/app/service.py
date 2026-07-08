from sqlalchemy.orm import Session

from app.models import Payment
from app.models import PaymentStatus

from app.schemas import PaymentRequest


class PaymentService:

    @staticmethod
    def process_payment(db: Session, request: PaymentRequest):

        payment = Payment(
            order_id=request.order_id,
            amount=request.amount,
            status=PaymentStatus.SUCCESS,
        )

        db.add(payment)

        db.commit()

        db.refresh(payment)

        return payment

    @staticmethod
    def refund(db: Session, order_id: int):

        payment = db.query(Payment).filter(Payment.order_id == order_id).first()

        if payment:

            payment.status = PaymentStatus.REFUNDED

            db.commit()

            db.refresh(payment)

        return payment

    @staticmethod
    def get_all(db: Session):

        return db.query(Payment).all()
