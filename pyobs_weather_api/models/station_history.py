from typing import Dict, List, Union

from pyobs_weather_api.models import Station
from pyobs_weather_api.models.history_data import HistoryData


class StationHistory:
    def __init__(self, station_data: Dict[Station, List[HistoryData]]):
        self._station_data: Dict[Station, List[HistoryData]] = station_data

    def get_stations(self) -> List[Station]:
        return list(self._station_data.keys())

    def _get_station_data_by_station(self, station: Station) -> List[HistoryData]:
        return self._station_data[station]

    def _get_station_data_by_code(self, code: str) -> List[HistoryData]:
        for key, item in self._station_data.items():
            if key.code == code:
                return item

        raise KeyError()

    def get_station_data(self, station: Union[str, Station]) -> List[HistoryData]:
        if isinstance(station, str):
            return self._get_station_data_by_code(station)

        return self._get_station_data_by_station(station)

