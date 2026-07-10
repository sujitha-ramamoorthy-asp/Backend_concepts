import strawberry

from graphql_types import Employee
from graphql_types import Department

from employee_service import EmployeeService
from department_service import DepartmentService


@strawberry.type
class Mutation:

    # ==================================================
    # Employee Mutations
    # ==================================================

    @strawberry.mutation
    def add_employee(
        self,
        id: int,
        name: str,
        salary: int
    ) -> Employee:

        return EmployeeService.add_employee(
            id,
            name,
            salary
        )

    @strawberry.mutation
    def update_employee(
        self,
        id: int,
        name: str,
        salary: int
    ) -> Employee:

        return EmployeeService.update_employee(
            id,
            name,
            salary
        )

    @strawberry.mutation
    def delete_employee(
        self,
        id: int
    ) -> bool:

        return EmployeeService.delete_employee(id)

    @strawberry.mutation
    def create_employee_file(self) -> bool:

        return EmployeeService.create_employee_file()

    @strawberry.mutation
    def delete_employee_file(self) -> bool:

        return EmployeeService.delete_employee_file()


    # ==================================================
    # Department Mutations
    # ==================================================

    @strawberry.mutation
    def add_department(
        self,
        id: int,
        name: str
    ) -> Department:

        return DepartmentService.add_department(
            id,
            name
        )

    @strawberry.mutation
    def update_department(
        self,
        id: int,
        name: str
    ) -> Department:

        return DepartmentService.update_department(
            id,
            name
        )

    @strawberry.mutation
    def delete_department(
        self,
        id: int
    ) -> bool:

        return DepartmentService.delete_department(id)

    @strawberry.mutation
    def create_department_file(self) -> bool:

        return DepartmentService.create_department_file()

    @strawberry.mutation
    def delete_department_file(self) -> bool:

        return DepartmentService.delete_department_file()