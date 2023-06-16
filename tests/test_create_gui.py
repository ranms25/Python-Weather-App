import pytest
import time
from weather_app import create_gui
from tkinter import Tk


def test_create_gui():
    duration = 10  # Set the duration in seconds
    
    start_time = time.time()
    end_time = start_time + duration
    
    root = Tk()
    create_gui()
    root.after(duration * 1000, root.destroy)  # Destroy the window after the specified duration in milliseconds
    
    while time.time() < end_time:
        root.update_idletasks()
        root.update()
