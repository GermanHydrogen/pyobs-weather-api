import datetime
from typing import Optional

from pyobs_weather_api.models import SensorType


class Sensor:
    def __init__(self,
                 name: str,
                 code: SensorType,
                 value: float, unit: str,
                 time: Optional[datetime.datetime],
                 good: Optional[bool],
                 since: Optional[datetime.datetime]):

        self._name = name
        self._type_code = code
        self._value = value
        self._unit = unit
        self._time = time
        self._good = good
        self._since = since

    @property
    def name(self):
        return self._name

    @property
    def type_code(self):
        return self._type_code

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @property
    def time(self):
        return self._time

    @property
    def time(self) -> Optional[datetime.datetime]:
        return self._time

    @property
    def good(self) -> Optional[bool]:
        return self._good

    @property
    def since(self) -> Optional[datetime.datetime]:
        return self._since
