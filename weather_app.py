import requests
import json
from dotenv import load_dotenv
import os


def get_weather_data(location):
    # Retrieve the API key from the environment variable
    api_key = os.getenv("API_KEY")

    # Construct the API URL with the location and API key
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    # Send a GET request to the API
    response = requests.get(api_url)

    # Parse the API response
    data = json.loads(response.text)

    # Extract the relevant weather information
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather_conditions = data["weather"][0]["description"]

    # Print the weather information
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity}%")
    print(f"Weather Conditions: {weather_conditions}")


def main():
    location = input("Enter a location: ")
    get_weather_data(location)


if __name__ == "__main__":
    # Load the environment variables from the .env file
    load_dotenv()

    main()