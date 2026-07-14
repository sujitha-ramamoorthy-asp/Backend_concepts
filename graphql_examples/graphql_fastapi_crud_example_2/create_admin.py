from database import SessionLocal

from services.auth_service import AuthService


db = SessionLocal()

AuthService.register(

    db,

    username="admin",

    password="admin123",

    role="ADMIN"

)

db.close()

print("Admin Created")