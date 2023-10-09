from typing import List, Dict

from pyobs_weather_api.models import HistoryData


class History:
    def __init__(self, data: List[HistoryData]):
        self._data = data

    @property
    def data(self):
        return self._data

    def get_raw(self) -> List[Dict]:
        return [
            x.to_dict() for x in self._data
        ]

    def as_pandas(self):
        import pandas as pd

        df = pd.DataFrame(self.get_raw())
        df.set_index("time", inplace=True)

        return df

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return str(self)