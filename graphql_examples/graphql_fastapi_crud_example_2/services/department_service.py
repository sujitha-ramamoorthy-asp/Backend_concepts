from repositories.department_repository import DepartmentRepository


class DepartmentService:

    @staticmethod
    def get_all(db):
        return DepartmentRepository.get_all(db)

    @staticmethod
    def get_by_id(db, department_id):
        return DepartmentRepository.get_by_id(
            db,
            department_id
        )
    
    @staticmethod
    def create(db, name):

        if not name.strip():
            raise Exception("Department name cannot be empty")

        return DepartmentRepository.create(
            db,
            name
        )