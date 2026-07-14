from strawberry.dataloader import DataLoader


def create_director_loader(db):


    async def load_directors(
        keys: list[int]
    ):

        from app.models import Director


        directors = (
            db.query(Director)
            .filter(
                Director.id.in_(keys)
            )
            .all()
        )


        director_map = {
            director.id: director
            for director in directors
        }


        return [
            director_map.get(key)
            for key in keys
        ]


    return DataLoader(
        load_fn=load_directors
    )