from database import SessionLocal

from services.auth_service import AuthService


db = SessionLocal()

AuthService.register(
    db,
    username="john",
    password="john123",
    role="USER"
)

db.close()