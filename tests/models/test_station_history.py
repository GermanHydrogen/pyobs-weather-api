from pyobs_weather_api.models import StationHistory, Station, HistoryData


def test_get_stations():
    station = Station("Observer", "observer")
    history = StationHistory(
        {
            station: []
        }
    )

    assert history.get_stations()[0] == station


def test_get_station_data(mock_data):
    station = Station("Observer", "observer")
    data = [mock_data]
    history = StationHistory(
        {
            station: data
        }
    )

    assert history.get_station_data(station)[0] == mock_data


def test_get_station_data_by_code(mock_data):
    data = [mock_data]
    history = StationHistory(
        {
            Station("Observer", "observer"): data
        }
    )

    assert history.get_station_data("observer")[0] == mock_data
