import strawberry

from app.models import Director
from app.models import Movie


@strawberry.type
class DirectorType:

    id: int

    name: str

    country: str


@strawberry.type
class MovieType:

    id: int

    title: str

    release_year: int

    rating: float

    director: DirectorType