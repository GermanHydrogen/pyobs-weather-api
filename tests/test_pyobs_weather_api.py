import pytest
from pyobs_weather_api import PyobsWeatherApi
from pyobs_weather_api.models import SensorType


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
