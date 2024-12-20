from peewee import CharField, Model

from capture.dependencies import db


class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db


def get_user_by_username(username: str) -> User | None:
    try:
        user = User.select().where(User.username == username).get()
    except User.DoesNotExist:
        return None

    return user
