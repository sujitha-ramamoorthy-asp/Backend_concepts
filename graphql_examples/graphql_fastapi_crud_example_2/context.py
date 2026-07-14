from fastapi import Request
from sqlalchemy.orm import Session
from strawberry.fastapi import BaseContext


class GraphQLContext(BaseContext):

    def __init__(
        self,
        request: Request,
        db: Session,
        user=None,
    ):

        self.request = request
        self.db = db
        self.user = user