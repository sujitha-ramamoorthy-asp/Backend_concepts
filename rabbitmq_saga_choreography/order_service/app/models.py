from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

from .database import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    customer = Column(
        String(100)
    )

    amount = Column(
        Float
    )

    status = Column(
        String(30),
        default="PENDING"
    )