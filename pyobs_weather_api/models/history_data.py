import datetime


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