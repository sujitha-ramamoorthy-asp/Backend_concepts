from app.repositories.director_repository import DirectorRepository


class DirectorService:

    @staticmethod
    def get_all(db):

        return DirectorRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        director_id,
    ):

        return DirectorRepository.get_by_id(
            db,
            director_id,
        )

    @staticmethod
    def create(
        db,
        name,
        country,
    ):

        return DirectorRepository.create(
            db,
            name,
            country,
        )

    @staticmethod
    def update(
        db,
        director_id,
        name,
        country,
    ):

        return DirectorRepository.update(
            db,
            director_id,
            name,
            country,
        )

    @staticmethod
    def delete(
        db,
        director_id,
    ):

        return DirectorRepository.delete(
            db,
            director_id,
        )