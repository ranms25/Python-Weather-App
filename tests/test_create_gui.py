import unittest
from weather_app import create_gui
from unittest.mock import patch, MagicMock

class TestWeatherAppGUI(unittest.TestCase):

    @patch('weather_app.load_dotenv')
    @patch('weather_app.ThemedTk')
    def test_create_gui(self, mock_ThemedTk, mock_load_dotenv):
        # Call the create_gui() function
        create_gui()

        # Assert that the necessary GUI elements and widgets are created
        mock_ThemedTk.assert_called_once_with(theme="Adapta")
        mock_root = mock_ThemedTk.return_value
        mock_root.geometry.assert_called_once_with("400x400")
        mock_root.resizable.assert_called_once_with(0, 0)
        mock_root.title.assert_called_once_with("Weather App")

if __name__ == '__main__':
    unittest.main()
