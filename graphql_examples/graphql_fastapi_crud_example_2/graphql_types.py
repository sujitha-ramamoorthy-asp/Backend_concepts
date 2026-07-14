import strawberry
import enum
from typing import List

@strawberry.type
class DepartmentType:

    id: int

    name: str

    employees: List["EmployeeType"]

@strawberry.type
class EmployeeType:

    id: int

    name: str

    salary: int

    department: DepartmentType


@strawberry.type
class TokenType:

    access_token: str = strawberry.field(name="accessToken")

    token_type: str = strawberry.field(name="tokenType")

@strawberry.type
class UserType:

    id: int

    username: str

    role: str

@strawberry.enum
class EmployeeSortField(enum.Enum):
    ID = "id"
    NAME = "name"
    SALARY = "salary"


@strawberry.enum
class SortOrder(enum.Enum):
    ASC = "asc"
    DESC = "desc"

@strawberry.type
class EmployeePage:

    total_count: int = strawberry.field(name="totalCount")

    page: int

    page_size: int = strawberry.field(name="pageSize")

    total_pages: int = strawberry.field(name="totalPages")

    items: list[EmployeeType]


@strawberry.input
class EmployeeInput:

    name: str

    salary: int

    department_id: int