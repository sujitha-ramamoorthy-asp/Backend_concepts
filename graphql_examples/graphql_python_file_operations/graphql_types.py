import strawberry


# ===========================================
# Employee GraphQL Type
# ===========================================

@strawberry.type
class Employee:
    id: int
    name: str
    salary: int


# ===========================================
# Department GraphQL Type
# ===========================================

@strawberry.type
class Department:
    id: int
    name: str