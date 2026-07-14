from app.repositories.movie_repository import MovieRepository


class MovieService:

    @staticmethod
    def get_all(db):

        return MovieRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        movie_id,
    ):

        return MovieRepository.get_by_id(
            db,
            movie_id,
        )

    @staticmethod
    def create(
        db,
        title,
        release_year,
        rating,
        director_id,
    ):

        return MovieRepository.create(
            db,
            title,
            release_year,
            rating,
            director_id,
        )

    @staticmethod
    def update(
        db,
        movie_id,
        title,
        release_year,
        rating,
        director_id,
    ):

        return MovieRepository.update(
            db,
            movie_id,
            title,
            release_year,
            rating,
            director_id,
        )

    @staticmethod
    def delete(
        db,
        movie_id,
    ):

        return MovieRepository.delete(
            db,
            movie_id,
        )

    @staticmethod
    def search(
        db,
        text,
    ):

        return MovieRepository.search(
            db,
            text,
        )