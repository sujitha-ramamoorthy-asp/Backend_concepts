from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100))

    customer_email = Column(String(100))

    product_name = Column(String(100))

    quantity = Column(Integer)

    status = Column(String(50), default="Created")