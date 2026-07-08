from enum import Enum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Enum as SqlEnum

from app.database import Base


class PaymentStatus(str, Enum):

    SUCCESS = "SUCCESS"

    REFUNDED = "REFUNDED"


class Payment(Base):

    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, nullable=False)

    amount = Column(Float, nullable=False)

    status = Column(
        SqlEnum(PaymentStatus), default=PaymentStatus.SUCCESS, nullable=False
    )
