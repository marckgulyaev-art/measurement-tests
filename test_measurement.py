import pytest
from measurement import diagnose_measurement

@pytest.mark.parametrize("value", [0, 50, 100])
def test_valid_temperature(value):
    assert diagnose_measurement(
        {"id": 1, "value": value, "received": True}
    ) == "| Status: OK | Message: Normal"

@pytest.mark.parametrize("value", [-1, 100.1, 105])
def test_OUT_OF_RANGE(value):
    assert diagnose_measurement(
        {"id": 2, "value": value, "received": True}
    ) == "| Status: OUT OF RANGE | Message: Invalid temperature"

@pytest.mark.parametrize("value", [50, -10, 105])
def test_NO_DATA(value):
    assert diagnose_measurement(
        {"id": 3, "value": value, "received": False}
    ) == "| Status: NO DATA | Message: Communication error"

@pytest.mark.parametrize("measurement, expected", [
	(
        	{"id": 4, "value": 'error', "received": True},
    		"| Status: INVALID DATA | Message: Invalid value type"
	),
	(
        	{"id": 5, "value": None, "received": True},
    		"| Status: INVALID DATA | Message: Missing value"
	),
	(
        	{"id": 6, "received": True},
		"| Status: INVALID DATA | Message: Missing field"
	)

])
def test_invalid_data(measurement, expected):
    assert diagnose_measurement(measurement) == expected