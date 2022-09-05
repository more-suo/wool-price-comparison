from freezegun import freeze_time

from src.utils import get_now_timestamp, normalize_stock_data


@freeze_time("1984-07-27")
def test_get_now_timestamp():
    assert get_now_timestamp() == "27-Jul-1984_00-00-00"


def test_normalize_stock_data():
    assert normalize_stock_data("Lieferbar") == "in stock"
    assert (
        normalize_stock_data("Halten Sie mich auf dem Laufenden")
        == "out of stock for now"
    )
    assert normalize_stock_data("Begrenzter Vorrat: 2") == "2 left"
