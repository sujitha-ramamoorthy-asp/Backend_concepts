from models import Employee


class EmployeeRepository:

    @staticmethod
    def get_all(db):

        return db.query(Employee).all()

    @staticmethod
    def get_by_id(db, id):

        return db.query(Employee).filter(
            Employee.id == id
        ).first()

    @staticmethod
    def create(
        db,
        id,
        name,
        salary
    ):

        emp = Employee(
            id=id,
            name=name,
            salary=salary
        )

        db.add(emp)

        db.commit()

        db.refresh(emp)

        return emp

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