import strawberry

from employee_query import EmployeeQuery
from department_query import DepartmentQuery


@strawberry.type
class Query(
    EmployeeQuery,
    DepartmentQuery
):
    pass