from datetime import datetime, timedelta

import bcrypt
from capture.data.accounts import User, get_user_by_username
from capture.dependencies import ALGORITHM, Settings
from jose import jwt

ACCESS_TOKEN_EXPIRE_MINUTES = 30

settings = Settings()


class InvalidUser(Exception):
    """Raised when the username or password is incorrect"""


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def authenticate_user(username: str, password: str) -> User:
    """
    For a given username and password, verify the details are correct.

    Raises:
        AuthError if login details are invalid
    """

    user = get_user_by_username(username)
    if user is None:
        raise InvalidUser("Username is not recognised")

    if not verify_password(password, user.password):
        raise InvalidUser("Password is incorrect")

    return user


def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=ALGORITHM)
    return encoded_jwt
