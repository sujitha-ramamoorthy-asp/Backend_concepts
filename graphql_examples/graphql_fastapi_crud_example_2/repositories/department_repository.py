from models import Department
from sqlalchemy.orm import joinedload

class DepartmentRepository:

    # @staticmethod
    # def get_all(db):
    #     return db.query(Department).all()

    @staticmethod
    def get_all(db):

        return (
            db.query(Department)
            .options(joinedload(Department.employees))
            .all()
        )

    @staticmethod
    def get_by_id(db, department_id):
        return (
            db.query(Department)
            .filter(Department.id == department_id)
            .first()
        )
    
    @staticmethod
    def create(db, name):

        department = Department(
            name=name
        )

        db.add(department)

        db.commit()

        db.refresh(department)

        return department