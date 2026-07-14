from functools import wraps

from graphql import GraphQLError

from exceptions import GraphQLException


def handle_graphql_exception(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:

            return func(*args, **kwargs)

        except GraphQLException as e:

            raise GraphQLError(
                message=e.message,
                extensions={
                    "code": e.code
                }
            )

    return wrapper