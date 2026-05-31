"""
Homework 8: Streamlit weather map and data visualization app.
Author: Budai Krisztian
"""

from lib.weather_dashboard_app import WeatherDashboardApp
from lib.weather_dashboard_app_config import WeatherDashboardAppConfig

if __name__ == "__main__":
    app_config = WeatherDashboardAppConfig()

    WeatherDashboardApp(app_config).run()
