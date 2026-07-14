from app.models import Director


class DirectorRepository:

    @staticmethod
    def get_all(db):

        return (
            db.query(Director)
            .all()
        )

    @staticmethod
    def get_by_id(db, director_id):

        return (
            db.query(Director)
            .filter(
                Director.id == director_id
            )
            .first()
        )

    @staticmethod
    def create(db, name, country):

        director = Director(
            name=name,
            country=country,
        )

        db.add(director)

        db.commit()

        db.refresh(director)

        return director

    @staticmethod
    def update(
        db,
        director_id,
        name,
        country,
    ):

        director = DirectorRepository.get_by_id(
            db,
            director_id,
        )

        if director is None:
            return None

        director.name = name
        director.country = country

        db.commit()

        db.refresh(director)

        return director

    @staticmethod
    def delete(
        db,
        director_id,
    ):

        director = DirectorRepository.get_by_id(
            db,
            director_id,
        )

        if director is None:
            return False

        db.delete(director)

        db.commit()

        return True