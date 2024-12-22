import datetime as dt

from capture.data import accounts as data_accounts
from capture.data import assets as data_assets
from capture.domain import accounts
from pydantic import BaseModel


class ChargeEvent(BaseModel):
    occurred_at: dt.datetime
    direction: str
    charge_percent: int


class Asset(BaseModel):
    serial_number: str
    voltage: int
    current: int
    capacity_kwh: int
    events: list[ChargeEvent]


class Property(BaseModel):
    address: str
    user: accounts.User | None
    assets: list[Asset]


def get_property_and_assets_for_customer(user_id: int) -> Property | None:
    properties = (
        data_assets.Property.select(
            data_assets.Property, data_assets.Asset, data_assets.ChargeEvent
        )
        .join(data_assets.Property)
        .join(data_assets.Asset)
        .join(data_assets.ChargeEvent)
        .where(data_accounts.User.id == user_id)
    )

    result = []
    for data_property in properties:
        user = accounts.User(username=property.user.username, password=None)

        property = Property(
            address=data_property.address,
            user=user,
        )

        for data_asset in data_property.assets:
            a
