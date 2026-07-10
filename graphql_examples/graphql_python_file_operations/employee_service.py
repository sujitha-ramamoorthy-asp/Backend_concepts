from employee_repository import EmployeeRepository


class EmployeeService:

    # ----------------------------------------
    # Read Employees
    # ----------------------------------------
    @staticmethod
    def get_employees():

        return EmployeeRepository.read_employees()

    # ----------------------------------------
    # Add Employee
    # ----------------------------------------
    @staticmethod
    def add_employee(
        id: int,
        name: str,
        salary: int
    ):

        # Business Validation
        if salary <= 0:
            raise Exception("Salary must be greater than zero.")

        return EmployeeRepository.add_employee(
            id,
            name,
            salary
        )

    # ----------------------------------------
    # Update Employee
    # ----------------------------------------
    @staticmethod
    def update_employee(
        id: int,
        name: str,
        salary: int
    ):

        if salary <= 0:
            raise Exception("Salary must be greater than zero.")

        return EmployeeRepository.update_employee(
            id,
            name,
            salary
        )

    # ----------------------------------------
    # Delete Employee
    # ----------------------------------------
    @staticmethod
    def delete_employee(
        id: int
    ):

        return EmployeeRepository.delete_employee(id)

    # ----------------------------------------
    # Create Employee File
    # ----------------------------------------
    @staticmethod
    def create_employee_file():

        return EmployeeRepository.create_employee_file()

    # ----------------------------------------
    # Delete Employee File
    # ----------------------------------------
    @staticmethod
    def delete_employee_file():

        return EmployeeRepository.delete_employee_file()