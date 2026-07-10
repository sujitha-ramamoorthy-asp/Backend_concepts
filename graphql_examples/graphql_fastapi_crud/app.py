from fastapi import FastAPI

from strawberry.fastapi import GraphQLRouter

from database import Base
from database import engine

from schema import schema

Base.metadata.create_all(bind=engine)

app = FastAPI()

graphql_app = GraphQLRouter(schema)

app.include_router(
    graphql_app,
    prefix="/graphql"
)