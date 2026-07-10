import strawberry

from graphql_types import Employee
from employee_service import EmployeeService


@strawberry.type
class EmployeeQuery:

    @strawberry.field
    def employees(self) -> list[Employee]:

        return EmployeeService.get_employees()