from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app.schemas import PaymentRequest
from app.schemas import PaymentResponse

from app.service import PaymentService

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/payment", response_model=PaymentResponse)
def payment(request: PaymentRequest, db: Session = Depends(get_db)):

    return PaymentService.process_payment(db, request)


@app.post("/refund/{order_id}", response_model=PaymentResponse)
def refund(order_id: int, db: Session = Depends(get_db)):

    payment = PaymentService.refund(db, order_id)

    if not payment:

        raise HTTPException(404, "Payment not found")

    return payment


@app.get("/payments", response_model=list[PaymentResponse])
def get_payments(db: Session = Depends(get_db)):

    return PaymentService.get_all(db)
