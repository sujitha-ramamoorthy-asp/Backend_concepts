from enum import Enum

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Enum as SqlEnum

from app.database import Base


class OrderStatus(str, Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100), nullable=False)

    product_name = Column(String(100), nullable=False)

    quantity = Column(Integer, nullable=False)

    amount = Column(Float, nullable=False)

    status = Column(
        SqlEnum(OrderStatus),
        default=OrderStatus.PENDING,
        nullable=False
    )