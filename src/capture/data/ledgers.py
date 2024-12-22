from enum import Enum

from capture.data import assets
from capture.dependencies import db
from peewee import CharField, ForeignKeyField, IntegerField, Model


class LedgerItemType(Enum):
    ASSET_PURCHASE = "ASSET_PURCHASE"
    ENERGY_PURCHASE = "ENERGY_PURCHASE"

    ENERGY_SALE = "ENERGY_SALE"

    @classmethod
    def choices(cls):
        return tuple((member.value, member.name) for member in cls)


class Ledger(Model):
    user = ForeignKeyField(assets.Property, backref="ledgers", unique=True)

    class Meta:
        database = db


class LedgerItem(Model):
    leger = ForeignKeyField(Ledger, backref="items")

    # Negative amounts indicate a charge (e.g. buying energy or initial asset purchase)
    amount = IntegerField()
    item_type = CharField(choices=LedgerItemType.choices())

    class Meta:
        database = db
