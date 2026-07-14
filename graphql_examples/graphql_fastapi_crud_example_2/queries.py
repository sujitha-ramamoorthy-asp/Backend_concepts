import strawberry
from strawberry.types import Info
from permissions import require_role

from graphql_types import EmployeeType
from graphql_types import UserType
from graphql_types import DepartmentType

from database import SessionLocal

from services.employee_service import EmployeeService
from graphql_types import EmployeeSortField
from graphql_types import SortOrder
from graphql_types import EmployeePage
from services.department_service import DepartmentService
from exceptions import AuthenticationException
from decorators import handle_graphql_exception


@strawberry.type
class Query:

    # @strawberry.field
    # def employees(
    #     self,
    #     info: Info,
    #     name: str | None = None,
    #     min_salary: int | None = None,
    #     max_salary: int | None = None,
    #     sort_by: EmployeeSortField | None = None,
    #     sort_order: SortOrder = SortOrder.ASC,
    # ) -> list[EmployeeType]:

    #     require_role(
    #         info,
    #         ["ADMIN", "USER"]
    #     )

    #     db = SessionLocal()

    #     try:

    #         return EmployeeService.get_all(
    #             db,
    #             name=name,
    #             min_salary=min_salary,
    #             max_salary=max_salary,
    #             sort_by=sort_by,
    #             sort_order=sort_order,
    #             )

    #     finally:

    #         db.close()

    @strawberry.field
    @handle_graphql_exception
    def employees(
        self,
        info: Info,
        name: str | None = None,
        department_id: int | None = None,
        min_salary: int | None = None,
        max_salary: int | None = None,
        sort_by: EmployeeSortField | None = None,
        sort_order: SortOrder = SortOrder.ASC,
        page: int = 1,
        page_size: int = 10
    ) -> EmployeePage:

        require_role(
            info,
            ["ADMIN", "USER"]
        )

        #db = SessionLocal()

        #try:
        db = info.context.db
        result =  EmployeeService.get_all(
            db,
            name=name,
            department_id=department_id,
            min_salary=min_salary,
            max_salary=max_salary,
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            page_size=page_size
            )
        return EmployeePage(

        total_count=result["total_count"],

        page=result["page"],

        page_size=result["page_size"],

        total_pages=result["total_pages"],

        items=result["employees"],

        )

        #finally:

            # db.close()

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

    
    @strawberry.field
    def me(self, info: Info) -> UserType:

        user = info.context.user

        if user is None:
            raise AuthenticationException("Authentication required")

        return UserType(
            id=user.id,
            username=user.username,
            role=user.role,
        )
    
    @strawberry.field
    def departments(
        self,
        info: Info,
    ) -> list[DepartmentType]:

        require_role(info, ["ADMIN", "USER"])

        db = SessionLocal()

        try:

            return DepartmentService.get_all(db)

        finally:

            db.close()