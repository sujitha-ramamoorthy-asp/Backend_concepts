import strawberry

from graphql_types import EmployeeType

from database import SessionLocal

from services.employee_service import EmployeeService


@strawberry.type
class Mutation:

    @strawberry.mutation
    def create_employee(
        self,
        id: int,
        name: str,
        salary: int
    ) -> EmployeeType:

        db = SessionLocal()

        try:
            return EmployeeService.create(
                db,
                id,
                name,
                salary
            )

        finally:
            db.close()

    @strawberry.mutation
    def update_employee(
        self,
        id: int,
        name: str,
        salary: int
    ) -> EmployeeType | None:

        db = SessionLocal()

        try:
            return EmployeeService.update(
                db,
                id,
                name,
                salary
            )

        finally:
            db.close()

    @strawberry.mutation
    def delete_employee(
        self,
        id: int
    ) -> bool:

        db = SessionLocal()

        try:
            return EmployeeService.delete(
                db,
                id
            )

        finally:
            db.close()