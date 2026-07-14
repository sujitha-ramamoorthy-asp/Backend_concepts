from app.repositories.actor_repository import ActorRepository


class ActorService:

    @staticmethod
    def get_all(db):

        return ActorRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        actor_id,
    ):

        return ActorRepository.get_by_id(
            db,
            actor_id,
        )

    @staticmethod
    def create(
        db,
        name,
        age,
    ):

        return ActorRepository.create(
            db,
            name,
            age,
        )

    @staticmethod
    def update(
        db,
        actor_id,
        name,
        age,
    ):

        return ActorRepository.update(
            db,
            actor_id,
            name,
            age,
        )

    @staticmethod
    def delete(
        db,
        actor_id,
    ):

        return ActorRepository.delete(
            db,
            actor_id,
        )

    @staticmethod
    def search(
        db,
        text,
    ):

        return ActorRepository.search(
            db,
            text,
        )