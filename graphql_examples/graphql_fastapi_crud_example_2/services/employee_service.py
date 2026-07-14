from repositories.employee_repository import EmployeeRepository
from repositories.department_repository import DepartmentRepository
from math import ceil
from graphql_types import EmployeeInput
from exceptions import ValidationException, NotFoundException


class EmployeeService:

    @staticmethod
    def get_all(
        db,
        name=None,
        department_id = None,
        min_salary=None,
        max_salary=None,
        sort_by=None,
        sort_order=None,
        page=1,
        page_size=10,
    ):
        # Validation
        if page < 1:
            raise Exception("page must be greater than 0")

        if page_size < 1:
            raise Exception("page_size must be greater than 0")

        if page_size > 100:
            raise Exception("page_size cannot exceed 100")

        # return EmployeeRepository.get_all(
        #     db=db,
        #     name=name,
        #     min_salary=min_salary,
        #     max_salary=max_salary,
        #     sort_by=sort_by,
        #     sort_order=sort_order,
        #     page=page,
        #     page_size=page_size,
        # )
        result = EmployeeRepository.get_all(
            db=db,
            name=name,
            min_salary=min_salary,
            max_salary=max_salary,
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            page_size=page_size,
        )

        total_pages = ceil(
            result["total_count"] / page_size
        ) if result["total_count"] else 0

        return {
            "employees": result["employees"],
            "total_count": result["total_count"],
            "page": page,
            "page_size": page_size,
            "total_pages": total_pages,
        }

    @staticmethod
    def get_by_id(db, id):

        return EmployeeRepository.get_by_id(db, id)
    
    # @staticmethod
    # def create(
    #     db,
    #     name,
    #     salary,
    #     department_id
    # ):
    #     if salary <= 0:
    #         raise Exception("Invalid salary")

    #     department = DepartmentRepository.get_by_id(
    #         db,
    #         department_id,
    #     )

    #     if department is None:
    #         raise Exception("Department not found")

    #     return EmployeeRepository.create(
    #         db=db,
    #         name=name,
    #         salary=salary,
    #         department=department,
    #     )

    @staticmethod
    def create(
        db,
        input: EmployeeInput,
    ):

        if input.salary <= 0:
            raise ValidationException(
        "Salary must be greater than zero"
    )

        department = DepartmentRepository.get_by_id(
            db,
            input.department_id,
        )

        if department is None:
            raise NotFoundException("Department not found")

        return EmployeeRepository.create(
            db=db,
            name=input.name,
            salary=input.salary,
            department=department,
        )

    @staticmethod
    def update(
        db,
        id,
        name,
        salary
    ):

        return EmployeeRepository.update(
            db,
            id,
            name,
            salary
        )

    @staticmethod
    def delete(
        db,
        id
    ):

        return EmployeeRepository.delete(
            db,
            id
        )