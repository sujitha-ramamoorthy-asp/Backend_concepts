from app.models import Series


class SeriesRepository:


    @staticmethod
    def get_all(db):

        return (
            db.query(Series)
            .all()
        )


    @staticmethod
    def get_by_id(
        db,
        series_id,
    ):

        return (
            db.query(Series)
            .filter(
                Series.id == series_id
            )
            .first()
        )


    @staticmethod
    def create(
        db,
        title,
        release_year,
        seasons,
        director_id,
    ):

        series = Series(
            title=title,
            release_year=release_year,
            seasons=seasons,
            director_id=director_id,
        )

        db.add(series)

        db.commit()

        db.refresh(series)

        return series


    @staticmethod
    def update(
        db,
        series_id,
        title,
        release_year,
        seasons,
        director_id,
    ):

        series = SeriesRepository.get_by_id(
            db,
            series_id,
        )

        if series is None:
            return None


        series.title = title
        series.release_year = release_year
        series.seasons = seasons
        series.director_id = director_id


        db.commit()

        db.refresh(series)

        return series


    @staticmethod
    def delete(
        db,
        series_id,
    ):

        series = SeriesRepository.get_by_id(
            db,
            series_id,
        )

        if series is None:
            return False


        db.delete(series)

        db.commit()

        return True


    @staticmethod
    def search(
        db,
        text,
    ):

        return (
            db.query(Series)
            .filter(
                Series.title.ilike(
                    f"%{text}%"
                )
            )
            .all()
        )