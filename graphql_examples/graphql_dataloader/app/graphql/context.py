from strawberry.fastapi import BaseContext

from app.loaders.director_loader import (
    create_director_loader
)

from app.loaders.actor_loader import (
    create_actor_loader
)


class GraphQLContext(BaseContext):

    def __init__(
        self,
        db,
        user=None,
    ):

        self.db = db

        self.user = user


        self.director_loader = (
            create_director_loader(db)
        )


        self.actor_loader = (
            create_actor_loader(db)
        )