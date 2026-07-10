import strawberry

@strawberry.type
class EmployeeType:

    id: int

    name: str

    salary: int