from department_repository import DepartmentRepository


class DepartmentService:

    # ----------------------------------------
    # Read Departments
    # ----------------------------------------
    @staticmethod
    def get_departments():

        return DepartmentRepository.read_departments()

    # ----------------------------------------
    # Add Department
    # ----------------------------------------
    @staticmethod
    def add_department(
        id: int,
        name: str
    ):

        if len(name.strip()) == 0:
            raise Exception("Department name cannot be empty.")

        return DepartmentRepository.add_department(
            id,
            name
        )

    # ----------------------------------------
    # Update Department
    # ----------------------------------------
    @staticmethod
    def update_department(
        id: int,
        name: str
    ):

        if len(name.strip()) == 0:
            raise Exception("Department name cannot be empty.")

        return DepartmentRepository.update_department(
            id,
            name
        )

    # ----------------------------------------
    # Delete Department
    # ----------------------------------------
    @staticmethod
    def delete_department(
        id: int
    ):

        return DepartmentRepository.delete_department(id)

    # ----------------------------------------
    # Create Department File
    # ----------------------------------------
    @staticmethod
    def create_department_file():

        return DepartmentRepository.create_department_file()

    # ----------------------------------------
    # Delete Department File
    # ----------------------------------------
    @staticmethod
    def delete_department_file():

        return DepartmentRepository.delete_department_file()