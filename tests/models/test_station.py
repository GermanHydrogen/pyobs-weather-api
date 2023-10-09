from pyobs_weather_api.models import Station


def test_name():
    name = "Boltwood II"
    code = "boltwood"

    station = Station(name, code)

    assert station.name == name


def test_code():
    name = "Boltwood II"
    code = "boltwood"

    station = Station(name, code)

    assert station.code == code
