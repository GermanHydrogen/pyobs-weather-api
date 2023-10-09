from pyobs_weather_api.models import History


def test_get_data(mock_data):
    history = History([mock_data])

    assert history.data[0] == mock_data


def test_get_raw(mock_data):
    history = History([mock_data])
    raw_history = history.get_raw()

    assert raw_history[0]["time"] == mock_data.time
    assert raw_history[0]["value"] == mock_data.value
    assert raw_history[0]["min"] == mock_data.min
    assert raw_history[0]["max"] == mock_data.max


def test_as_pandas(mock_data):
    history = History([mock_data])
    df = history.as_pandas()

    assert df.index[0] == mock_data.time
    assert df.iloc[0]["value"] == mock_data.value
    assert df.iloc[0]["min"] == mock_data.min
    assert df.iloc[0]["max"] == mock_data.max


def test_str(mock_data):
    history = History([mock_data])

    assert (history.__repr__() ==
            f"[Time: 31.12.2000 23:30:10\t Value: {mock_data._value}\t Min: {mock_data._min}\t Max: {mock_data._max}]")
