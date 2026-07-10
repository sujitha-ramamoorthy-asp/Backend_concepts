import strawberry

from graphql_types import EmployeeType

from database import SessionLocal

from services.employee_service import EmployeeService


@strawberry.type
class Query:

    @strawberry.field
    def employees(self) -> list[EmployeeType]:

        db = SessionLocal()

        try:
            return EmployeeService.get_all(db)

        finally:
            db.close()

    @strawberry.field
    def employee(
        self,
        id: int
    ) -> EmployeeType | None:

        db = SessionLocal()

        try:
            return EmployeeService.get_by_id(
                db,
                id
            )

        finally:
            db.close()