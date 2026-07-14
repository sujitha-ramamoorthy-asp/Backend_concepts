import strawberry

from strawberry.types import Info

from app.graphql.types import (
    DirectorType,
    MovieType,
    SeriesType,
    ActorType,
)

from app.graphql.inputs import (
    DirectorInput,
    MovieInput,
    SeriesInput,
    ActorInput,
)

from app.graphql.mappers import Mapper

from app.services.director_service import DirectorService
from app.services.movie_service import MovieService
from app.services.series_service import SeriesService
from app.services.actor_service import ActorService


@strawberry.type
class Mutation:


    # =====================================================
    # Director Mutations
    # =====================================================

    @strawberry.mutation
    def create_director(
        self,
        info: Info,
        input: DirectorInput,
    ) -> DirectorType:

        director = DirectorService.create(
            info.context.db,
            input.name,
            input.country,
        )

        return Mapper.director(director)


    @strawberry.mutation
    def update_director(
        self,
        info: Info,
        id: int,
        input: DirectorInput,
    ) -> DirectorType | None:

        director = DirectorService.update(
            info.context.db,
            id,
            input.name,
            input.country,
        )

        return Mapper.director(director)


    @strawberry.mutation
    def delete_director(
        self,
        info: Info,
        id: int,
    ) -> bool:

        return DirectorService.delete(
            info.context.db,
            id,
        )


    # =====================================================
    # Movie Mutations
    # =====================================================

    @strawberry.mutation
    def create_movie(
        self,
        info: Info,
        input: MovieInput,
    ) -> MovieType:

        movie = MovieService.create(
            info.context.db,
            input.title,
            input.release_year,
            input.rating,
            input.director_id,
        )

        return Mapper.movie(movie)


    @strawberry.mutation
    def update_movie(
        self,
        info: Info,
        id: int,
        input: MovieInput,
    ) -> MovieType | None:

        movie = MovieService.update(
            info.context.db,
            id,
            input.title,
            input.release_year,
            input.rating,
            input.director_id,
        )

        return Mapper.movie(movie)


    @strawberry.mutation
    def delete_movie(
        self,
        info: Info,
        id: int,
    ) -> bool:

        return MovieService.delete(
            info.context.db,
            id,
        )


    # =====================================================
    # Series Mutations
    # =====================================================

    @strawberry.mutation
    def create_series(
        self,
        info: Info,
        input: SeriesInput,
    ) -> SeriesType:

        series = SeriesService.create(
            info.context.db,
            input.title,
            input.release_year,
            input.seasons,
            input.director_id,
        )

        return Mapper.series(series)


    @strawberry.mutation
    def update_series(
        self,
        info: Info,
        id: int,
        input: SeriesInput,
    ) -> SeriesType | None:

        series = SeriesService.update(
            info.context.db,
            id,
            input.title,
            input.release_year,
            input.seasons,
            input.director_id,
        )

        return Mapper.series(series)


    @strawberry.mutation
    def delete_series(
        self,
        info: Info,
        id: int,
    ) -> bool:

        return SeriesService.delete(
            info.context.db,
            id,
        )


    # =====================================================
    # Actor Mutations
    # =====================================================

    @strawberry.mutation
    def create_actor(
        self,
        info: Info,
        input: ActorInput,
    ) -> ActorType:

        actor = ActorService.create(
            info.context.db,
            input.name,
            input.age,
        )

        return Mapper.actor(actor)


    @strawberry.mutation
    def update_actor(
        self,
        info: Info,
        id: int,
        input: ActorInput,
    ) -> ActorType | None:

        actor = ActorService.update(
            info.context.db,
            id,
            input.name,
            input.age,
        )

        return Mapper.actor(actor)


    @strawberry.mutation
    def delete_actor(
        self,
        info: Info,
        id: int,
    ) -> bool:

        return ActorService.delete(
            info.context.db,
            id,
        )