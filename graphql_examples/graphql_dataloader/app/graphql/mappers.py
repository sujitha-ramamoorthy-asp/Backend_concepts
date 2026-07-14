from app.graphql.types import (
    DirectorType,
    MovieType,
    SeriesType,
    ActorType,
)


class Mapper:

    # ==========================================================
    # Director
    # ==========================================================

    @staticmethod
    def director(director):

        if director is None:
            return None

        return DirectorType(
            id=director.id,
            name=director.name,
            country=director.country,
        )

    @staticmethod
    def directors(directors):

        return [
            Mapper.director(director)
            for director in directors
        ]

    # ==========================================================
    # Movie
    # ==========================================================

    @staticmethod
    def movie(movie):

        if movie is None:
            return None

        return MovieType(
            id=movie.id,
            title=movie.title,
            release_year=movie.release_year,
            rating=movie.rating,
            director_id=movie.director_id
        )

    @staticmethod
    def movies(movies):

        return [
            Mapper.movie(movie)
            for movie in movies
        ]

    # ==========================================================
    # Series
    # ==========================================================

    @staticmethod
    def series(series):

        if series is None:
            return None

        return SeriesType(
            id=series.id,
            title=series.title,
            release_year=series.release_year,
            seasons=series.seasons,
            director=Mapper.director(series.director),
        )

    @staticmethod
    def all_series(series_list):

        return [
            Mapper.series(series)
            for series in series_list
        ]

    # ==========================================================
    # Actor
    # ==========================================================

    @staticmethod
    def actor(actor):

        if actor is None:
            return None

        return ActorType(
            id=actor.id,
            name=actor.name,
            age=actor.age,
        )

    @staticmethod
    def actors(actors):

        return [
            Mapper.actor(actor)
            for actor in actors
        ]