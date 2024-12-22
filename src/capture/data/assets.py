from enum import Enum

from capture.data import accounts
from capture.dependencies import db
from peewee import CharField, DateTimeField, ForeignKeyField, IntegerField, Model


class Direction(Enum):
    IMPORT = "IMPORT"
    EXPORT = "EXPORT"

    @classmethod
    def choices(cls):
        return tuple((member.value, member.name) for member in cls)


class Property(Model):
    address = CharField()
    user = ForeignKeyField(accounts.User, backref="properties")

    class Meta:
        database = db


class Asset(Model):
    property = ForeignKeyField(Property, backref="assets")
    serial_number = CharField()
    voltage = IntegerField()
    current = IntegerField()
    capacity_kwh = IntegerField()

    class Meta:
        database = db


class ChargeEvent(Model):
    asset = ForeignKeyField(Asset, backref="events")
    occurred_at = DateTimeField()
    direction = CharField(choices=Direction.choices())
    charge_percent = IntegerField()

    class Meta:
        database = db
