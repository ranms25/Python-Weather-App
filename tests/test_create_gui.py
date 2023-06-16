import pytest
from weather_app import create_gui
from tkinter import Tk


def test_create_gui():
    root = Tk()
    create_gui()
    root.after(1000, root.destroy)  # Delay the destruction of the window