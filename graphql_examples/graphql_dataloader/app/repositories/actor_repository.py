from app.models import Actor


class ActorRepository:

    @staticmethod
    def get_all(db):

        return (
            db.query(Actor)
            .all()
        )

    @staticmethod
    def get_by_id(db, actor_id):

        return (
            db.query(Actor)
            .filter(
                Actor.id == actor_id
            )
            .first()
        )

    @staticmethod
    def create(
        db,
        name,
        age,
    ):

        actor = Actor(
            name=name,
            age=age,
        )

        db.add(actor)

        db.commit()

        db.refresh(actor)

        return actor

    @staticmethod
    def update(
        db,
        actor_id,
        name,
        age,
    ):

        actor = ActorRepository.get_by_id(
            db,
            actor_id,
        )

        if actor is None:
            return None

        actor.name = name
        actor.age = age

        db.commit()

        db.refresh(actor)

        return actor

    @staticmethod
    def delete(
        db,
        actor_id,
    ):

        actor = ActorRepository.get_by_id(
            db,
            actor_id,
        )

        if actor is None:
            return False

        db.delete(actor)

        db.commit()

        return True

    @staticmethod
    def search(
        db,
        text,
    ):

        return (
            db.query(Actor)
            .filter(
                Actor.name.ilike(f"%{text}%")
            )
            .all()
        )