import datetime

import pytest

from pyobs_weather_api.models import HistoryData


@pytest.fixture(scope="module")
def mock_data():
    return HistoryData(datetime.datetime.strptime("31-12-2000T23:30:10", "%d-%m-%YT%H:%M:%S"),
                       10.0, 9.0, 11.0)