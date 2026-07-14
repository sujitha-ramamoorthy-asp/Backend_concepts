from repositories.user_repository import UserRepository

from security import (
    hash_password,
    verify_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    def register(
        db,
        username,
        password,
        role,
    ):

        existing = UserRepository.get_by_username(
            db,
            username,
        )

        if existing:
            raise Exception("User already exists")

        hashed = hash_password(password)

        return UserRepository.create_user(
            db,
            username,
            hashed,
            role,
        )

    @staticmethod
    def login(
        db,
        username,
        password,
    ):

        user = UserRepository.get_by_username(
            db,
            username,
        )

        if user is None:
            raise Exception("Invalid username")

        if not verify_password(
            password,
            user.password,
        ):
            raise Exception("Invalid password")

        token = create_access_token(
            {
                "username": user.username,
                "role": user.role,
            }
        )

        return {
            "access_token": token,
            "token_type": "Bearer",
        }