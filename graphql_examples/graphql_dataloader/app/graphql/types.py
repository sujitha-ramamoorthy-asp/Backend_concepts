import strawberry

from app.models import Director
from app.models import Movie

from app.graphql.interfaces import Content
from strawberry.types import Info

@strawberry.type
class DirectorType:

    id: int

    name: str

    country: str


# @strawberry.type
# class MovieType:

#     id: int

#     title: str

#     release_year: int

#     rating: int

#     director: DirectorType

# @strawberry.type
# class MovieType(Content):

#     rating: float

#     director: DirectorType

@strawberry.type
class MovieType:

    id: int

    title: str

    release_year: int

    rating: float


    director_id: int


    @strawberry.field
    async def director(
        self,
        info: Info
    ) -> DirectorType:


        return await (
            info.context
            .director_loader
            .load(self.director_id)
        )

@strawberry.type
class SeriesType(Content):

    seasons: int

    director_id: int


    @strawberry.field
    async def director(
        self,
        info: Info,
    ) -> "DirectorType":

        return await (
            info.context
            .director_loader
            .load(self.director_id)
        )

@strawberry.type
class ActorType:

    id: int

    name: str

    age: int