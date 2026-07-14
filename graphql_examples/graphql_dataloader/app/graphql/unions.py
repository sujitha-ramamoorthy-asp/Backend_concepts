from typing import Annotated, Union

import strawberry

from app.graphql.types import (
    MovieType,
    SeriesType,
    ActorType,
)


SearchResult = Annotated[
    Union[
        MovieType,
        SeriesType,
        ActorType,
    ],
    strawberry.union("SearchResult"),
]