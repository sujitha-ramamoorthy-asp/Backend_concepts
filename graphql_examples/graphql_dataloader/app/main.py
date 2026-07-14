from fastapi import FastAPI, Request

from strawberry.fastapi import GraphQLRouter

from app.graphql.schema import schema

from app.database import SessionLocal

from app.graphql.context import GraphQLContext


app = FastAPI()


async def get_context(
    request: Request,
):

    db = SessionLocal()

    return GraphQLContext(
        db=db,
        user=None,
    )


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)


app.include_router(
    graphql_app,
    prefix="/graphql"
)