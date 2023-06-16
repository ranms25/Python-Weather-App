import pytest
import os
import requests
from weather_app import get_weather_data

class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    def raise_for_status(self):
        if self.status_code != 200:
            raise requests.exceptions.HTTPError

def test_get_weather_data(monkeypatch):
    api_key = os.getenv("API_KEY")
    mock_api_key = api_key
    mock_location = "New York"
    expected_url = f"http://api.openweathermap.org/data/2.5/weather?q={mock_location}&appid={mock_api_key}"

    mock_response = {
        "weather": [{"icon": "01d", "description": "clear sky"}],
        "main": {"temp": 293.15, "humidity": 50},
        "wind": {"speed": 3.5, "deg": 180},
        "rain": {"1h": 0.0},
        "snow": {"1h": 0.0}
    }

    def mock_get(url):
        assert url == expected_url
        return MockResponse(mock_response, 200)

    monkeypatch.setattr("requests.get", mock_get)

    weather_data, _ = get_weather_data(mock_location)

    assert weather_data == "Temperature: 293.15 K\n" \
                           "Temperature (Celsius): 20.0 °C\n" \
                           "Humidity: 50%\n" \
                           "Weather Conditions: clear sky\n" \
                           "Wind Speed: 3.5 m/s\n" \
                           "Wind Direction: 180°\n" \
                           "Rainfall: 0.0 mm\n" \
                           "Snowfall: 0.0 mm"
