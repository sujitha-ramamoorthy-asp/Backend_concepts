import csv
import os

from graphql_types import Department

DEPARTMENT_FILE = "departments.csv"


class DepartmentRepository:

    # ----------------------------------------
    # Read All Departments
    # ----------------------------------------
    @staticmethod
    def read_departments() -> list[Department]:

        departments = []

        if not os.path.exists(DEPARTMENT_FILE):
            return departments

        with open(DEPARTMENT_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                departments.append(
                    Department(
                        id=int(row["id"]),
                        name=row["name"]
                    )
                )

        return departments

    # ----------------------------------------
    # Add Department
    # ----------------------------------------
    @staticmethod
    def add_department(
        id: int,
        name: str
    ) -> Department:

        with open(DEPARTMENT_FILE, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                id,
                name
            ])

        return Department(
            id=id,
            name=name
        )

    # ----------------------------------------
    # Update Department
    # ----------------------------------------
    @staticmethod
    def update_department(
        id: int,
        name: str
    ) -> Department:

        departments = []

        with open(DEPARTMENT_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if int(row["id"]) == id:
                    row["name"] = name

                departments.append(row)

        with open(DEPARTMENT_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "name"
                ]
            )

            writer.writeheader()

            writer.writerows(departments)

        return Department(
            id=id,
            name=name
        )

    # ----------------------------------------
    # Delete Department
    # ----------------------------------------
    @staticmethod
    def delete_department(
        id: int
    ) -> bool:

        departments = []

        with open(DEPARTMENT_FILE, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                if int(row["id"]) != id:
                    departments.append(row)

        with open(DEPARTMENT_FILE, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "id",
                    "name"
                ]
            )

            writer.writeheader()

            writer.writerows(departments)

        return True

    # ----------------------------------------
    # Create Department File
    # ----------------------------------------
    @staticmethod
    def create_department_file() -> bool:

        with open(DEPARTMENT_FILE, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "id",
                "name"
            ])

        return True

    # ----------------------------------------
    # Delete Department File
    # ----------------------------------------
    @staticmethod
    def delete_department_file() -> bool:

        if os.path.exists(DEPARTMENT_FILE):

            os.remove(DEPARTMENT_FILE)

            return True

        return False