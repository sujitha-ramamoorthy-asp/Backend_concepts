from repositories.employee_repository import EmployeeRepository


class EmployeeService:

    @staticmethod
    def get_all(db):

        return EmployeeRepository.get_all(db)

    @staticmethod
    def get_by_id(db, id):

        return EmployeeRepository.get_by_id(db, id)

    @staticmethod
    def create(
        db,
        id,
        name,
        salary
    ):

        if salary <= 0:
            raise Exception("Invalid Salary")

        return EmployeeRepository.create(
            db,
            id,
            name,
            salary
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