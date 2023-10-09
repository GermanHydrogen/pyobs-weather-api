import datetime

import pytest
from pyobs_weather_api.models import HistoryData


def test_time(mock_data):
    assert mock_data.time == datetime.datetime.strptime("31-12-2000T23:30:10", "%d-%m-%YT%H:%M:%S")


def test_value(mock_data):
    assert mock_data.value == 10.0


def test_min(mock_data):
    assert mock_data.min == 9.0


def test_max(mock_data):
    assert mock_data.max == 11.0
