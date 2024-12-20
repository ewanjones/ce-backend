# TODO: Make this a postgres DB
import os
from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from peewee import SqliteDatabase
from pydantic_settings import BaseSettings

from capture.domain import accounts

ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

db = SqliteDatabase("capture.db")


class Settings(BaseSettings):
    secret_key: str = "TESTING"


settings = Settings()


def get_current_user(token: str = Depends(oauth2_scheme)) -> accounts.User:
    # TODO: Fix this circular import
    from capture.data.accounts import User

    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        try:
            user = User.select().where(User.username == username).get()
        except User.DoesNotExist:
            raise HTTPException(
                status_code=401,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


GetCurrentUser = Annotated[accounts.User, Depends(get_current_user)]
