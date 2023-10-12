import datetime
from typing import List, Tuple, Union, Dict, Optional

from pyobs_weather_api.models import SensorType, Station, HistoryData, StationHistory
from pyobs_weather_api.models.history import History
from pyobs_weather_api.models.sensor import Sensor
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

    def _parse_sensor_data(self, data: Dict):
        name = data["name"]
        code: SensorType
        if "code" in data:
            code = SensorType(data["code"])
        else:
            code = SensorType(data["type_code"])

        value = data["value"]
        unit = data["unit"]

        time: Optional[datetime.datetime] = None
        if "time" in data:
            time = datetime.datetime.strptime(data["time"], self.TIME_FORMAT)

        good: Optional[bool] = data["good"]
        since: Optional[datetime.datetime] = None
        if good is not None:
            since = datetime.datetime.strptime(data["since"], "%Y-%m-%dT%H:%M:%S.%fZ")

        return Sensor(name, code, value, unit, time, good, since)

    def get_sensor(self, station: Union[Station, str], sensor_type: Union[SensorType, str]) -> Sensor:
        if isinstance(station, Station):
            station = station.code
        if isinstance(sensor_type, SensorType):
            sensor_type = sensor_type.value

        data = self._rest_adapter.get(f"stations/{station}/{sensor_type}")

        return self._parse_sensor_data(data)

    def _parse_history_data(self, data: Dict):
        time = datetime.datetime.strptime(data["time"], self.TIME_FORMAT)

        return HistoryData(time, data["value"], data["min"], data["max"])

    def _parse_station_history(self, data: Dict) -> StationHistory:
        history = {
            Station(x["name"], x["code"]):
                History([self._parse_history_data(y) for y in x["data"]])
            for x in data["stations"]}

        return StationHistory(history)

    def get_sensor_history(self, sensor: Union[SensorType, str],
                           interval: Tuple[datetime.datetime, datetime.datetime] = None) -> StationHistory:
        params = None
        if interval is not None:
            params = {
                "start": datetime.datetime.strftime(interval[0], self.TIME_FORMAT),
                "end": datetime.datetime.strftime(interval[1], self.TIME_FORMAT)
            }
        if isinstance(sensor, SensorType):
            sensor = sensor.value

        data = self._rest_adapter.get(f"history/{sensor}/", params)
        history = self._parse_station_history(data)

        return history
