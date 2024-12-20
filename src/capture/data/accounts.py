from peewee import Model, CharField
from capture.dependencies import db


class User(Model):
    username = CharField()
    password = CharField()

    class Meta:
        database = db
