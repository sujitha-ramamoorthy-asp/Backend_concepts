from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from .database import Base


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(Integer)

    product = Column(String(100))

    quantity = Column(Integer)

    status = Column(
        String(30),
        default="RESERVED"
    )