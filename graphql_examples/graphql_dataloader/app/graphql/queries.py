import strawberry

from strawberry.types import Info

from app.graphql.types import (
    DirectorType,
    MovieType,
    SeriesType,
    ActorType,
)

from app.graphql.unions import SearchResult

from app.graphql.mappers import Mapper

from app.services.director_service import DirectorService
from app.services.movie_service import MovieService
from app.services.series_service import SeriesService
from app.services.actor_service import ActorService
from app.services.search_service import SearchService


@strawberry.type
class Query:

    # =====================================================
    # Directors
    # =====================================================

    @strawberry.field
    def directors(
        self,
        info: Info,
    ) -> list[DirectorType]:

        directors = DirectorService.get_all(
            info.context.db
        )

        return Mapper.directors(directors)

    @strawberry.field
    def director(
        self,
        info: Info,
        id: int,
    ) -> DirectorType | None:

        director = DirectorService.get_by_id(
            info.context.db,
            id,
        )

        return Mapper.director(director)

    # =====================================================
    # Movies
    # =====================================================

    @strawberry.field
    def movies(
        self,
        info: Info,
    ) -> list[MovieType]:

        movies = MovieService.get_all(
            info.context.db
        )

        return Mapper.movies(movies)

    @strawberry.field
    def movie(
        self,
        info: Info,
        id: int,
    ) -> MovieType | None:

        movie = MovieService.get_by_id(
            info.context.db,
            id,
        )

        return Mapper.movie(movie)

    # =====================================================
    # Series
    # =====================================================

    @strawberry.field
    def series(
        self,
        info: Info,
    ) -> list[SeriesType]:

        series = SeriesService.get_all(
            info.context.db
        )

        return Mapper.all_series(series)

    @strawberry.field
    def series_by_id(
        self,
        info: Info,
        id: int,
    ) -> SeriesType | None:

        series = SeriesService.get_by_id(
            info.context.db,
            id,
        )

        return Mapper.series(series)

    # =====================================================
    # Actors
    # =====================================================

    @strawberry.field
    def actors(
        self,
        info: Info,
    ) -> list[ActorType]:

        actors = ActorService.get_all(
            info.context.db
        )

        return Mapper.actors(actors)

    @strawberry.field
    def actor(
        self,
        info: Info,
        id: int,
    ) -> ActorType | None:

        actor = ActorService.get_by_id(
            info.context.db,
            id,
        )

        return Mapper.actor(actor)

    # =====================================================
    # Search
    # =====================================================

    @strawberry.field
    def search(
        self,
        info: Info,
        text: str,
    ) -> list[SearchResult]:

        data = SearchService.search(
            info.context.db,
            text,
        )

        results = []

        results.extend(
            Mapper.movies(
                data["movies"]
            )
        )

        results.extend(
            Mapper.all_series(
                data["series"]
            )
        )

        results.extend(
            Mapper.actors(
                data["actors"]
            )
        )

        return results