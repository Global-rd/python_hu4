"""
Streamlit weather map and data visualization application.
"""

import streamlit as st

from .open_meteo import (
    CityLocation,
    ForecastData,
    ForecastParams,
    GeocodingSearchParams,
    OpenMeteoClient,
)
from .search_logger import SearchLogger
from .weather_dashboard_app_config import WeatherDashboardAppConfig
from .weather_dashboard_view import WeatherDashboardView


class WeatherDashboardApp:
    """Coordinate weather API calls, logging and dashboard rendering."""

    GEOCODING_RESULT_COUNT: int = 1
    GEOCODING_LANGUAGE: str = "en"
    GEOCODING_FORMAT: str = "json"
    CURRENT_VARIABLES: str = (
        "temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    HOURLY_VARIABLES: str = "temperature_2m"
    API_CACHE_TTL_SECONDS: int = 60 * 60

    def __init__(self, app_config: WeatherDashboardAppConfig) -> None:
        """Initialize the dashboard dependencies."""
        self.app_config: WeatherDashboardAppConfig = app_config
        self.search_logger: SearchLogger = SearchLogger()
        self.view: WeatherDashboardView = WeatherDashboardView(
            app_config.get_default_city(),
            app_config.get_forecast_days(),
        )

    @staticmethod
    @st.cache_data(ttl=API_CACHE_TTL_SECONDS, show_spinner=False)
    def _search_cities_cached(
        params: GeocodingSearchParams,
    ) -> list[CityLocation]:
        """Return cached geocoding results for one day."""
        return OpenMeteoClient().search_cities(params)

    @staticmethod
    @st.cache_data(ttl=API_CACHE_TTL_SECONDS, show_spinner=False)
    def _get_forecast_cached(params: ForecastParams) -> ForecastData:
        """Return cached forecast results for one day."""
        return OpenMeteoClient().get_forecast(params)

    @staticmethod
    def get_first_city(
        city_name: str,
        locations: list[CityLocation],
    ) -> CityLocation:
        """Return the first location matching the user's city search."""
        normalized_city_name = city_name.strip()

        if normalized_city_name == "":
            raise ValueError("Please enter a city name.")

        if not any(character.isalpha() for character in normalized_city_name):
            raise ValueError("City name must contain at least one letter.")

        if len(locations) == 0:
            raise ValueError(f"City not found: {normalized_city_name}")

        return locations[0]

    @staticmethod
    def _get_display_city(location: CityLocation) -> str:
        """Return a user-facing city and country label."""
        return f"{location['name']}, {location['country']}"

    def log_search(
        self,
        location: CityLocation,
        forecast: ForecastData,
    ) -> None:
        """Log one successful weather dashboard search."""
        current = forecast["current"]
        self.search_logger.log_search(
            self._get_display_city(location),
            current["temperature_2m"],
            current["relative_humidity_2m"],
            current["wind_speed_10m"],
        )

    def create_geocoding_search_params(
        self,
        city_name: str,
    ) -> GeocodingSearchParams:
        """Return Open-Meteo geocoding search params for the app."""
        return {
            "name": city_name.strip(),
            "count": self.GEOCODING_RESULT_COUNT,
            "language": self.GEOCODING_LANGUAGE,
            "format": self.GEOCODING_FORMAT,
        }

    def create_forecast_params(
        self,
        location: CityLocation,
    ) -> ForecastParams:
        """Return Open-Meteo forecast params for the app."""
        return {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": self.CURRENT_VARIABLES,
            "hourly": self.HOURLY_VARIABLES,
            "forecast_days": self.app_config.get_forecast_days(),
            "timezone": self.app_config.get_timezone(),
        }

    def run(self) -> None:
        """Run the Streamlit weather dashboard."""
        selected_city = self.view.render_layout()

        try:
            locations = self._search_cities_cached(
                self.create_geocoding_search_params(selected_city)
            )
            location = self.get_first_city(selected_city, locations)
            forecast = self._get_forecast_cached(
                self.create_forecast_params(location)
            )
            self.view.render_dashboard(location, forecast)
            self.log_search(location, forecast)
        except (RuntimeError, ValueError) as error:
            self.view.render_warning(str(error))
