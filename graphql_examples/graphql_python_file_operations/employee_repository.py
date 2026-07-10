import csv
import os

from graphql_types import Employee

EMPLOYEE_FILE = "employees.csv"


class EmployeeRepository:

    # ----------------------------------------
    # Read All Employees
    # ----------------------------------------
    @staticmethod
    def read_employees() -> list[Employee]:

        employees = []

        if not os.path.exists(EMPLOYEE_FILE):
            return employees

        with open(EMPLOYEE_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                employees.append(
                    Employee(
                        id=int(row["id"]),
                        name=row["name"],
                        salary=int(row["salary"])
                    )
                )

        return employees

    # ----------------------------------------
    # Add Employee
    # ----------------------------------------
    @staticmethod
    def add_employee(
        id: int,
        name: str,
        salary: int
    ) -> Employee:

        with open(EMPLOYEE_FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                id,
                name,
                salary
            ])

        return Employee(
            id=id,
            name=name,
            salary=salary
        )

    # ----------------------------------------
    # Update Employee
    # ----------------------------------------
    @staticmethod
    def update_employee(
        id: int,
        name: str,
        salary: int
    ) -> Employee:

        employees = []

        with open(EMPLOYEE_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if int(row["id"]) == id:

                    row["name"] = name
                    row["salary"] = salary

                employees.append(row)

        with open(EMPLOYEE_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "name",
                    "salary"
                ]
            )

            writer.writeheader()

            writer.writerows(employees)

        return Employee(
            id=id,
            name=name,
            salary=salary
        )

    # ----------------------------------------
    # Delete Employee
    # ----------------------------------------
    @staticmethod
    def delete_employee(id: int) -> bool:

        employees = []

        with open(EMPLOYEE_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if int(row["id"]) != id:
                    employees.append(row)

        with open(EMPLOYEE_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "name",
                    "salary"
                ]
            )

            writer.writeheader()

            writer.writerows(employees)

        return True

    # ----------------------------------------
    # Create Employee CSV File
    # ----------------------------------------
    @staticmethod
    def create_employee_file() -> bool:

        with open(EMPLOYEE_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "id",
                "name",
                "salary"
            ])

        return True

    # ----------------------------------------
    # Delete Employee CSV File
    # ----------------------------------------
    @staticmethod
    def delete_employee_file() -> bool:

        if os.path.exists(EMPLOYEE_FILE):

            os.remove(EMPLOYEE_FILE)

            return True

        return False