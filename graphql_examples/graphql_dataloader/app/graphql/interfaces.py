import strawberry


@strawberry.interface
class Content:

    id: int

    title: str

    release_year: int