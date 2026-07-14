from app.repositories.series_repository import SeriesRepository


class SeriesService:

    @staticmethod
    def get_all(db):

        return SeriesRepository.get_all(db)

    @staticmethod
    def get_by_id(
        db,
        series_id,
    ):

        return SeriesRepository.get_by_id(
            db,
            series_id,
        )

    @staticmethod
    def create(
        db,
        title,
        release_year,
        seasons,
        director_id,
    ):

        return SeriesRepository.create(
            db,
            title,
            release_year,
            seasons,
            director_id,
        )

    @staticmethod
    def update(
        db,
        series_id,
        title,
        release_year,
        seasons,
        director_id,
    ):

        return SeriesRepository.update(
            db,
            series_id,
            title,
            release_year,
            seasons,
            director_id,
        )

    @staticmethod
    def delete(
        db,
        series_id,
    ):

        return SeriesRepository.delete(
            db,
            series_id,
        )

    @staticmethod
    def search(
        db,
        text,
    ):

        return SeriesRepository.search(
            db,
            text,
        )