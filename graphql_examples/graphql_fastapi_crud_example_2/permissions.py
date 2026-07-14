from strawberry.types import Info
from exceptions import AuthenticationException


def require_authenticated(info: Info):

    user = info.context.user

    if user is None:
        raise AuthenticationException("Authentication required")

    return user


def require_role(info: Info, roles: list[str]):

    user = require_authenticated(info)

    if user.role not in roles:
        raise Exception(
            f"Access denied. Required role(s): {', '.join(roles)}"
        )

    return user