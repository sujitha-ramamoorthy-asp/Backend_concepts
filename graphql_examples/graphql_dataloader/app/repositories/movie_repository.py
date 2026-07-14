from app.models import Movie


class MovieRepository:


    @staticmethod
    def get_all(db):

        return (
            db.query(Movie)
            .all()
        )


    @staticmethod
    def get_by_id(
        db,
        id: int
    ):

        return (
            db.query(Movie)
            .filter(
                Movie.id == id
            )
            .first()
        )


    @staticmethod
    def create(
        db,
        movie: Movie
    ):

        db.add(movie)

        db.commit()

        db.refresh(movie)

        return movie


    @staticmethod
    def delete(
        db,
        movie: Movie
    ):

        db.delete(movie)

        db.commit()