from typing import List

from pyobs_weather_api.models import SensorType, Station
from pyobs_weather_api.rest_adapter import RestAdapter


class PyobsWeatherApi:
    def __init__(self, url: str, ssl_verify: bool = True):
        self._rest_adapter = RestAdapter(url, ssl_verify)

    def get_history_types(self) -> List[SensorType]:
        data = self._rest_adapter.get("history")

        history_types = [SensorType(name) for name in data]

        return history_types

    def get_stations(self) -> List[Station]:
        data = self._rest_adapter.get("stations")

        stations = [Station(**x) for x in data]

        return stations
