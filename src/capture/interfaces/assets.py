import datetime as dt

from capture.data.assets import Direction
from capture.domain import assets
from fastapi import APIRouter

assets_router = APIRouter(prefix="/assets")


@assets_router.get("/")
async def get_property_and_assets():
    event_1 = assets.ChargeEvent(
        occurred_at=dt.datetime(2024, 12, 22, 9),
        direction=Direction.IMPORT,
        charge_percent=100,
    )
    asset_1 = assets.Asset(
        serial_number="BAT001",
        voltage=51,
        current=80,
        capacity_kwh=9,
        events=[event_1],
    )
    event_2 = assets.ChargeEvent(
        occurred_at=dt.datetime(2024, 12, 22, 9),
        direction=Direction.IMPORT,
        charge_percent=68,
    )
    asset_2 = assets.Asset(
        serial_number="BAT002",
        voltage=20,
        current=60,
        capacity_kwh=7,
        events=[event_2],
    )
    _property = assets.Property(
        address="213A Lower Clapton Road, London, E5 8EG",
        user=None,
        assets=[asset_1, asset_2],
    )
    return [_property]
