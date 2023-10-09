from pyobs_weather_api import PyobsWeatherApi
from pyobs_weather_api.models import SensorType


def test_init():
    url = "weather.iag50srv.astro.physik.uni-goettingen.de"
    api = PyobsWeatherApi(url)

    assert api._rest_adapter._url == f"https://{url}/api/"


def test_get_history_types(mocker):
    api_result = ["temp", "rain", "press", "sunalt", "windspeed", "humid", "winddir", "skymag", "skytemp"]

    api = PyobsWeatherApi("")
    mocker.patch.object(api._rest_adapter, "get", return_value=api_result)

    history_types = api.get_history_types()
    all_types_check = [x in history_types for x in SensorType]

    assert False not in all_types_check
