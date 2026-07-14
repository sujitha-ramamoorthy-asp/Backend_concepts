from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Employee(Base):

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    salary = Column(Integer)

    department_id = Column(
    Integer,
    ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="employees"
    )


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    password = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )


class Department(Base):

    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    employees = relationship(
        "Employee",
        back_populates="department"
    )