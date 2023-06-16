import pytest
import time
from weather_app import create_gui
from tkinter import Tk


def test_create_gui():
    root = Tk()
    create_gui()

    timeout = 5  # Set the timeout duration in seconds
    start_time = time.time()

    while time.time() - start_time < timeout:
        root.update()

    root.destroy()
