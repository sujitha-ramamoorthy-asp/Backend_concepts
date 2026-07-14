import strawberry

from strawberry.types import Info

from permissions import require_role

from graphql_types import EmployeeType
from graphql_types import TokenType
from graphql_types import DepartmentType

from database import SessionLocal

from services.department_service import DepartmentService
from services.employee_service import EmployeeService
from services.auth_service import AuthService
from graphql_types import EmployeeInput
from decorators import handle_graphql_exception


@strawberry.type
class Mutation:

    @strawberry.mutation
    def login(
        self,
        username: str,
        password: str,
    ) -> TokenType:

        db = SessionLocal()

        try:

            token = AuthService.login(
                db,
                username,
                password,
            )

            return TokenType(
                access_token=token["access_token"],
                token_type=token["token_type"],
            )

        finally:

            db.close()

    # @strawberry.mutation
    # def create_employee(
    #     self,
    #     info: Info,
    #     name: str,
    #     salary: int,
    #     department_id: int,
    # ) -> EmployeeType:
        
    #     require_role(info, ["ADMIN"])

    #     db = SessionLocal()

    #     try:
    #         employee = EmployeeService.create(
    #             db,
    #             name,
    #             salary,
    #             department_id,
    #         )

    #         return employee

    #     finally:
    #         db.close()

    @strawberry.mutation
    @handle_graphql_exception
    def create_employee(
        self,
        info: Info,
        input: EmployeeInput,
    ) -> EmployeeType:

        require_role(info, ["ADMIN"])

        db = SessionLocal()

        try:

            return EmployeeService.create(
                db=db,
                input=input,
            )

        finally:

            db.close()

    @strawberry.mutation
    @handle_graphql_exception
    def update_employee(
        self,
        employee_id: int,
        info: Info,
        name: str,
        salary: int
    ) -> EmployeeType | None:
        
        require_role(info, ["ADMIN"])

        db = SessionLocal()

        try:
            return EmployeeService.update(
                db,
                employee_id,
                name,
                salary
            )

        finally:
            db.close()

    @strawberry.mutation
    @handle_graphql_exception
    def delete_employee(
        self,
        info: Info,
        employee_id: int
    ) -> bool:
        
        require_role(info, ["ADMIN"])

        db = SessionLocal()

        try:
            return EmployeeService.delete(
                db,
                employee_id
            )

        finally:
            db.close()

    
    @strawberry.mutation
    @handle_graphql_exception
    def create_department(
        self,
        info: Info,
        name: str,
    ) -> DepartmentType:

        require_role(info, ["ADMIN"])

        db = SessionLocal()

        try:

            return DepartmentService.create(
                db,
                name,
            )

        finally:

            db.close()