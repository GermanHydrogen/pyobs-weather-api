import pytest

from pyobs_weather_api.models import StationHistory, Station
from pyobs_weather_api.models.history import History


def test_get_stations():
    station = Station("Observer", "observer")
    history = StationHistory(
        {
            station: History([])
        }
    )

    assert history.get_stations()[0] == station


def test_get_station_data(mock_data):
    station = Station("Observer", "observer")
    data = [mock_data]
    history = StationHistory(
        {
            station: History(data)
        }
    )

    assert history.get_station_data(station).data[0] == mock_data


def test_get_station_data_by_code(mock_data):
    data = [mock_data]
    history = StationHistory(
        {
            Station("Observer", "observer"): History(data)
        }
    )

    assert history.get_station_data("observer").data[0] == mock_data


def test_get_station_data_by_code_not_found(mock_data):
    data = [mock_data]
    history = StationHistory(
        {
            Station("Observer", "observer"): History(data)
        }
    )

    with pytest.raises(KeyError):
        history.get_station_data("test")