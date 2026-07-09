from sqlalchemy import Column, Integer, String

from inventory_service.app.database import Base


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    product = Column(String(100))

    available_quantity = Column(Integer)