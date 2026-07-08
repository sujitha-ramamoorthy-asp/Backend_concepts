from enum import Enum

from sqlalchemy import Column
from sqlalchemy import Enum as SqlEnum
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class InventoryStatus(str, Enum):
    RESERVED = "RESERVED"
    FAILED = "FAILED"


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    order_id = Column(Integer, nullable=False)

    product_name = Column(String(100), nullable=False)

    quantity = Column(Integer, nullable=False)

    status = Column(SqlEnum(InventoryStatus), nullable=False)
