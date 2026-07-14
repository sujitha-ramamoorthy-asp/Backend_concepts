from fastapi import FastAPI, Depends
from fastapi import Request

from strawberry.fastapi import GraphQLRouter

from database import Base, get_db
from database import engine

from schema import schema

from auth import get_current_user
from context import GraphQLContext


Base.metadata.create_all(bind=engine)

app = FastAPI()


async def get_graphql_context(
    request: Request,
    db=Depends(get_db),
) -> GraphQLContext:

    authorization = request.headers.get("Authorization")

    user = None

    if authorization and authorization.startswith("Bearer "):

        token = authorization[7:]

        user = get_current_user(token)

    #return GraphQLContext(user=user)
    return GraphQLContext(
        request=request,
        db=db,
        user=user,
    )


graphql_app = GraphQLRouter(
    schema,
    context_getter=get_graphql_context
)

app.include_router(
    graphql_app,
    prefix="/graphql"
)