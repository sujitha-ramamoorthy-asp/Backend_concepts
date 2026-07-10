import strawberry

from graphql_types import Department
from department_service import DepartmentService


@strawberry.type
class DepartmentQuery:

    @strawberry.field
    def departments(self) -> list[Department]:

        return DepartmentService.get_departments()