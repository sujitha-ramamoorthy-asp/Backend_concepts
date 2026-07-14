from strawberry.dataloader import DataLoader


def create_actor_loader(db):


    async def load_actors(
        keys: list[int]
    ):

        from app.models import Actor


        actors = (
            db.query(Actor)
            .filter(
                Actor.id.in_(keys)
            )
            .all()
        )


        actor_map = {
            actor.id: actor
            for actor in actors
        }


        return [
            actor_map.get(key)
            for key in keys
        ]


    return DataLoader(
        load_fn=load_actors
    )