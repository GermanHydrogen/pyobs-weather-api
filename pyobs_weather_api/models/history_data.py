import datetime
from typing import Dict, Union


class HistoryData:
    def __init__(self, time: datetime.datetime, value: float, min: float, max: float):
        self._time = time
        self._value = value
        self._min = min
        self._max = max

    @property
    def time(self):
        return self._time

    @property
    def value(self):
        return self._value

    @property
    def min(self):
        return self._min

    @property
    def max(self):
        return self._max

    def to_dict(self) -> Dict[str, Union[datetime.datetime, float]]:
        return {
            "time": self._time,
            "value": self._value,
            "min": self._min,
            "max": self._max
        }

    def __str__(self):
        time_str = datetime.datetime.strftime(self._time, "%d.%m.%Y %H:%M:%S")
        return f"Time: {time_str}\t Value: {self._value}\t Min: {self._min}\t Max: {self._max}"

    def __repr__(self):
        return str(self)