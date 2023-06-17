
# Python-Weather-App
Python Weather App is a simple command-line application that allows users to retrieve the current weather information for a specified location. Built using Python, it utilizes a weather service API to fetch real-time weather data, including temperature, humidity, and weather conditions. This app retrieve weather information from [OpenWeatherMap(https://openweathermap.org/)

# Getting Started
### Installation
To get started, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer.
>**Note: This program might works only for windows os.**

## Dependencies
To install the required packages, open up your terminal or command prompt and navigate to the project's root directory. Then, run the following command:
```pip install -r requirements.txt```
As OpenWeather requires an API key, please request and use your [own API key](https://openweathermap.org/appid) for using this app.

## Usage
1. Clone or download the project and navigate to the root directory.
2. Add your own OpenWeather API key to the `.env` file. You can find the file [here](https://github.com/ranms25/Python-Weather-App/blob/main/.env).
3. Open the `weather_app.py` file and run it using Python.
4. The weather application window will open.
5. Enter the desired location in the location input field.
6. Click the "Get Weather" button to retrieve the weather information for the specified location.
7. The weather data will be displayed in the text field below, including temperature, humidity, weather conditions, wind speed, wind direction, rainfall, and snowfall.
8. An icon representing the weather conditions will also be displayed.
9. If there is an error retrieving the weather data, an error message will be displayed in the text field.

Please note that step 2 is important to ensure that the API key is provided so that the application can make requests to the OpenWeather API successfully.

## Test
To run the tests for the weather application on Windows:
1. Open a command prompt or terminal and navigate to the project's root directory.
2. Ensure that pytest is installed. If not, use `pip install pytest` to install it.
3. Run the tests using the command `pytest` in the command prompt or terminal.
