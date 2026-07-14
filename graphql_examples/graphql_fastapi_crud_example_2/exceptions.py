class GraphQLException(Exception):

    def __init__(
        self,
        message: str,
        code: str
    ):

        self.message = message
        self.code = code

        super().__init__(message)


class ValidationException(GraphQLException):

    def __init__(self, message):

        super().__init__(
            message,
            code="BAD_REQUEST"
        )


class AuthenticationException(GraphQLException):

    def __init__(self, message="Authentication required"):

        super().__init__(
            message,
            code="UNAUTHENTICATED"
        )


class AuthorizationException(GraphQLException):

    def __init__(self, message="Access denied"):

        super().__init__(
            message,
            code="FORBIDDEN"
        )


class NotFoundException(GraphQLException):

    def __init__(self, message):

        super().__init__(
            message,
            code="NOT_FOUND"
        )