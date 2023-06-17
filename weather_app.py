import os
import json
import tkinter as tk
from io import BytesIO
import requests
from dotenv import load_dotenv
from PIL import ImageTk, Image
from ttkthemes import ThemedTk


def get_weather_data(location):
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("API_KEY")

    if not api_key:
        raise ValueError("API key is missing. Please add it to the .env file.")

    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    response = requests.get(api_url)
    response.raise_for_status()  # Raise an exception for non-successful status codes

    data = response.json()

    weather_icon_code = data["weather"][0]["icon"]
    icon_url = f"http://openweathermap.org/img/w/{weather_icon_code}.png"

    temperature = data["main"]["temp"]
    temperature_celsius = round(temperature - 273.15, 2)
    humidity = data["main"]["humidity"]
    weather_conditions = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]
    wind_direction = data["wind"]["deg"]
    rainfall = data.get("rain", {}).get("1h", 0)
    snowfall = data.get("snow", {}).get("1h", 0)

    weather_data_string = (
        f"Temperature: {temperature} K\n"
        f"Temperature (Celsius): {temperature_celsius} °C\n"
        f"Humidity: {humidity}%\n"
        f"Weather Conditions: {weather_conditions}\n"
        f"Wind Speed: {wind_speed} m/s\n"
        f"Wind Direction: {wind_direction}°\n"
        f"Rainfall: {rainfall} mm\n"
        f"Snowfall: {snowfall} mm"
    )

    return weather_data_string, icon_url


def get_weather(location_entry, tfield, weather_icon_label):
    location = location_entry.get()
    try:
        weather_data, icon_url = get_weather_data(location)

        tfield.delete(1.0, tk.END)
        tfield.insert(tk.END, weather_data)

        response = requests.get(icon_url)
        response.raise_for_status()

        icon_image = Image.open(BytesIO(response.content))
        icon_image = icon_image.resize((50, 50))

        icon_image_tk = ImageTk.PhotoImage(icon_image)
        weather_icon_label.config(image=icon_image_tk)
        weather_icon_label.image = icon_image_tk
    except (requests.RequestException, json.JSONDecodeError, ValueError) as e:
        tfield.delete(1.0, tk.END)
        tfield.insert(tk.END, f"Error: {str(e)}")


def create_gui():
    load_dotenv()

    root = ThemedTk(theme="Adapta")
    root.geometry("400x400")
    root.resizable(0, 0)
    root.title("Weather App")

    container = tk.Frame(root)
    container.pack(pady=10)

    location_label = tk.Label(container, text="Location:")
    location_label.pack()

    location_entry = tk.Entry(container)
    location_entry.pack()

    get_weather_button = tk.Button(
        container,
        text="Get Weather",
        command=lambda: get_weather(location_entry, tfield, weather_icon_label)
    )
    get_weather_button.pack(pady=10)

    weather_icon_label = tk.Label(root)
    weather_icon_label.pack()

    weather_now = tk.Label(root, text="The Weather is:", font="arial 12 bold")
    weather_now.pack(pady=10)

    tfield = tk.Text(root, width=46, height=10)
    tfield.pack()

    root.mainloop()


if __name__ == "__main__":
    create_gui()
