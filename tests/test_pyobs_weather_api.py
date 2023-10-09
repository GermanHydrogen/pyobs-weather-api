import datetime

import pytest
from pyobs_weather_api import PyobsWeatherApi
from pyobs_weather_api.models import SensorType, StationHistory, Station


@pytest.fixture()
def api(request, mocker):
    url = "weather.iag50srv.astro.physik.uni-goettingen.de"
    api = PyobsWeatherApi(url)

    marker = request.node.get_closest_marker("api_result")
    mocker.patch.object(api._rest_adapter, "get", return_value=marker.args[0])

    return api


def test_init():
    url = "weather.iag50srv.astro.physik.uni-goettingen.de"
    api = PyobsWeatherApi(url)

    assert api._rest_adapter._url == f"https://{url}/api/"


@pytest.mark.api_result(["temp", "rain", "press", "sunalt", "windspeed", "humid", "winddir", "skymag", "skytemp"])
def test_get_history_types(api: PyobsWeatherApi):
    history_types = api.get_history_types()
    all_types_check = [x in history_types for x in SensorType]

    assert False not in all_types_check


@pytest.mark.api_result([{"name": "Observer", "code": "observer"}, {"name": "Average values", "code": "iag50cm_avg"}])
def test_get_stations(api):
    stations = api.get_stations()

    assert stations[0].name == "Observer"
    assert stations[0].code == "observer"

    assert stations[1].name == "Average values"
    assert stations[1].code == "iag50cm_avg"


@pytest.mark.api_result({"stations": [{"code": "lambrecht", "name": "Lambrecht", "color": "#B90e46", "data": [{"time": "2023-10-08T18:45:00Z", "value": 11.099999999999943, "min": 11.1, "max": 11.1}]}]})
def test_get_sensor_history_w_sensor_type(api):
    history: StationHistory = api.get_sensor_history(SensorType.SkyTemperature)

    assert history.get_station_data("lambrecht").data[0].value == 11.099999999999943
    assert history.get_station_data("lambrecht").data[0].time == datetime.datetime.strptime("2023-10-08T18:45:00Z", "%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.api_result({"stations": [{"code": "lambrecht", "name": "Lambrecht", "color": "#B90e46", "data": [{"time": "2023-10-08T18:45:00Z", "value": 11.099999999999943, "min": 11.1, "max": 11.1}]}]})
def test_get_sensor_history_w_string(api):
    history: StationHistory = api.get_sensor_history("lambrecht")

    assert history.get_station_data("lambrecht").data[0].value == 11.099999999999943
    assert history.get_station_data("lambrecht").data[0].time == datetime.datetime.strptime("2023-10-08T18:45:00Z", "%Y-%m-%dT%H:%M:%SZ")


@pytest.mark.api_result({"stations": [{"code": "lambrecht", "name": "Lambrecht", "color": "#B90e46", "data": [{"time": "2023-10-08T18:45:00Z", "value": 11.099999999999943, "min": 11.1, "max": 11.1}]}]})
def test_get_sensor_history_w_intervall(api):
    history: StationHistory = api.get_sensor_history("lambrecht",
                                                     interval=(
                                                          datetime.datetime.strptime("2022-10-08T18:45:00Z",
                                                                                     "%Y-%m-%dT%H:%M:%SZ"),
                                                          datetime.datetime.strptime("2023-10-08T18:45:00Z",
                                                                                     "%Y-%m-%dT%H:%M:%SZ")
                                                      ))

    api._rest_adapter.get.assert_called_once_with("history/lambrecht/", {
        "start": "2022-10-08T18:45:00Z",
        "end": "2023-10-08T18:45:00Z"
    })
