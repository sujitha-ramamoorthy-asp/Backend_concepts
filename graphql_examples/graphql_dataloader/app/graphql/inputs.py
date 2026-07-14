import strawberry


@strawberry.input
class DirectorInput:

    name: str
    country: str


@strawberry.input
class MovieInput:

    title: str
    release_year: int
    rating: float
    director_id: int


@strawberry.input
class SeriesInput:

    title: str
    release_year: int
    seasons: int
    director_id: int


@strawberry.input
class ActorInput:

    name: str
    age: int