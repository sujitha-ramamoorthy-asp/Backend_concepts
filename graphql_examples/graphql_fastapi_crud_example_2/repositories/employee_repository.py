from models import Employee
from graphql_types import EmployeeSortField
from graphql_types import SortOrder
from graphql_types import EmployeePage
from math import ceil
from sqlalchemy.orm import joinedload

class EmployeeRepository:

    # @staticmethod
    # def get_all(
    #     db,
    #     name=None,
    #     min_salary=None,
    #     max_salary=None,
    #     sort_by=None,
    #     sort_order=None,
    # ):

    #     query = db.query(Employee)

    #     # -------------------
    #     # Filtering
    #     # -------------------

    #     if name:
    #         query = query.filter(
    #             Employee.name.ilike(f"%{name}%")
    #         )

    #     if min_salary is not None:
    #         query = query.filter(
    #             Employee.salary >= min_salary
    #         )

    #     if max_salary is not None:
    #         query = query.filter(
    #             Employee.salary <= max_salary
    #         )

    #     # -------------------
    #     # Sorting
    #     # -------------------

    #     if sort_by:

    #         column_map = {

    #             EmployeeSortField.ID: Employee.id,

    #             EmployeeSortField.NAME: Employee.name,

    #             EmployeeSortField.SALARY: Employee.salary,

    #         }

    #         column = column_map[sort_by]
    #         print(column_map)
    #         print(sort_by)
    #         print(column)

    #         if sort_order == SortOrder.DESC:

    #             query = query.order_by(column.desc())

    #         else:

    #             query = query.order_by(column.asc())

    #     return query.all()



    @staticmethod
    def get_all(
        db,
        name=None,
        department_id=None,
        min_salary=None,
        max_salary=None,
        sort_by=None,
        sort_order=None,
        page=1,
        page_size=10,
    ):

        query = (
            db.query(Employee)
            .options(joinedload(Employee.department))
        )

        # -------------------------
        # Filtering
        # -------------------------

        if name:
            query = query.filter(
                Employee.name.ilike(f"%{name}%")
            )

        if department_id is not None:
            query = query.filter(
                Employee.department_id == department_id
            )

        if min_salary is not None:
            query = query.filter(
                Employee.salary >= min_salary
            )

        if max_salary is not None:
            query = query.filter(
                Employee.salary <= max_salary
            )

        # -------------------------
        # Sorting
        # -------------------------

        if sort_by:

            column_map = {
                EmployeeSortField.ID: Employee.id,
                EmployeeSortField.NAME: Employee.name,
                EmployeeSortField.SALARY: Employee.salary,
            }

            column = column_map[sort_by]

            if sort_order == SortOrder.DESC:
                query = query.order_by(column.desc())
            else:
                query = query.order_by(column.asc())

        # -------------------------
        # Count
        # -------------------------

        total_count = query.count()

        # -------------------------
        # Pagination
        # -------------------------

        offset = (page - 1) * page_size

        employees = (
            query
            .offset(offset)
            .limit(page_size)
            .all()
        )

        # Repository returns only data
        return {
            "employees": employees,
            "total_count": total_count
        }

    @staticmethod
    def get_by_id(db, id):

        return db.query(Employee).filter(
            Employee.id == id
        ).first()

    @staticmethod
    def create(db, name, salary, department):

        employee = Employee(
            name=name,
            salary=salary,
            department=department
        )

        db.add(employee)
        db.commit()
        db.refresh(employee)

        employee = (
            db.query(Employee)
            .options(joinedload(Employee.department))
            .filter(Employee.id == employee.id)
            .first()
        )

        return employee

    @staticmethod
    def update(
        db,
        id,
        name,
        salary
    ):

        emp = db.query(Employee).filter(
            Employee.id == id
        ).first()

        if not emp:
            return None

        emp.name = name
        emp.salary = salary

        db.commit()

        db.refresh(emp)

        return emp

    @staticmethod
    def delete(
        db,
        id
    ):

        emp = db.query(Employee).filter(
            Employee.id == id
        ).first()

        if not emp:
            return False

        db.delete(emp)

        db.commit()

        return True