from capture.data.ledgers import LedgerItemType


def test_ledger_item_choices():
    assert LedgerItemType.choices() == (
        ("ASSET_PURCHASE", "ASSET_PURCHASE"),
        ("ENERGY_PURCHASE", "ENERGY_PURCHASE"),
        ("ENERGY_SALE", "ENERGY_SALE"),
    )
