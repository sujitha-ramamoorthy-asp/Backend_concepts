# from datetime import datetime
# from datetime import timedelta

# from jose import jwt
# from jose import JWTError

# from passlib.context import CryptContext

# from config import settings


# pwd_context = CryptContext(
#     schemes=["bcrypt"],
#     deprecated="auto"
# )


# # --------------------------------------
# # Hash Password
# # --------------------------------------
# def hash_password(password: str):

#     return pwd_context.hash(password)


# # --------------------------------------
# # Verify Password
# # --------------------------------------
# def verify_password(
#     plain_password: str,
#     hashed_password: str
# ):

#     return pwd_context.verify(
#         plain_password,
#         hashed_password
#     )


# # --------------------------------------
# # Create JWT Token
# # --------------------------------------
# def create_access_token(data: dict):

#     payload = data.copy()

#     expire = datetime.utcnow() + timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
#     )

#     payload["exp"] = expire

#     token = jwt.encode(
#         payload,
#         settings.SECRET_KEY,
#         algorithm=settings.ALGORITHM
#     )

#     return token


# # --------------------------------------
# # Verify JWT
# # --------------------------------------
# def verify_access_token(token: str):

#     try:

#         payload = jwt.decode(
#             token,
#             settings.SECRET_KEY,
#             algorithms=[settings.ALGORITHM]
#         )

#         return payload

#     except JWTError:

#         return None

import bcrypt

from datetime import datetime
from datetime import timedelta

from jose import jwt
from jose import JWTError

from config import settings


# ----------------------------------------
# Hash Password
# ----------------------------------------

def hash_password(password: str) -> str:

    hashed = bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


# ----------------------------------------
# Verify Password
# ----------------------------------------

def verify_password(
    plain_password: str,
    hashed_password: str
) -> bool:

    return bcrypt.checkpw(

        plain_password.encode("utf-8"),

        hashed_password.encode("utf-8")

    )


# ----------------------------------------
# Create JWT
# ----------------------------------------

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload["exp"] = expire

    token = jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

    return token


# ----------------------------------------
# Verify JWT
# ----------------------------------------

def verify_access_token(token: str):

    try:

        payload = jwt.decode(

            token,

            settings.SECRET_KEY,

            algorithms=[settings.ALGORITHM]

        )

        return payload

    except JWTError:

        return None