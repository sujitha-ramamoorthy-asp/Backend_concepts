from database import SessionLocal

from repositories.user_repository import UserRepository

from security import verify_access_token


def get_current_user(token: str):

    payload = verify_access_token(token)

    if payload is None:

        return None

    username = payload.get("username")

    if username is None:

        return None

    db = SessionLocal()

    try:

        user = UserRepository.get_current_user(
            db,
            username
        )

        return user

    finally:

        db.close()