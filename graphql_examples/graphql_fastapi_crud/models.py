from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    salary = Column(Integer)