from models import User


class UserRepository:

    @staticmethod
    def get_by_username(
        db,
        username
    ):

        return db.query(User).filter(
            User.username == username
        ).first()

    @staticmethod
    def create_user(
        db,
        username,
        password,
        role
    ):

        user = User(

            username=username,

            password=password,

            role=role

        )

        db.add(user)

        db.commit()

        db.refresh(user)

        return user
    
    @staticmethod
    def get_current_user(
        db,
        username
    ):

        return (
            db.query(User)
            .filter(User.username == username)
            .first()
        )