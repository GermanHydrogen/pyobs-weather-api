import datetime
from typing import List, Tuple, Union, Dict

from pyobs_weather_api.models import SensorType, Station, HistoryData, StationHistory
from pyobs_weather_api.rest_adapter import RestAdapter


class PyobsWeatherApi:
    TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

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

    def _parse_history_data(self, data: Dict):
        time = datetime.datetime.strptime(data["time"], self.TIME_FORMAT)

        return HistoryData(time, data["value"], data["min"], data["max"])

    def _parse_station_history(self, data: Dict) -> StationHistory:
        history = {
            Station(x["name"], x["code"]):
                [self._parse_history_data(y) for y in x["data"]]
            for x in data["stations"]}

        return StationHistory(history)

    def get_station_history(self, station: Union[Station, str],
                            interval: Tuple[datetime.datetime, datetime.datetime] = None):
        params = None
        if interval is not None:
            params = {
                "start": datetime.datetime.strftime(interval[0], self.TIME_FORMAT),
                "end": datetime.datetime.strftime(interval[1], self.TIME_FORMAT)
            }
        if isinstance(station, Station):
            station = station.code

        data = self._rest_adapter.get(f"history/{station}/", params)
        history = self._parse_station_history(data)

        return history
