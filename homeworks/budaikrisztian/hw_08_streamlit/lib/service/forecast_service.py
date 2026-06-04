"""
Forecast service for the weather dashboard.
"""

import streamlit as st

from ..app_types import DashboardLocation
from ..open_meteo import ForecastData, ForecastParams, OpenMeteoClient


class ForecastService:
    """Fetch and cache Open-Meteo forecast data for dashboard locations."""

    CURRENT_VARIABLES: str = (
        "temperature_2m,relative_humidity_2m,wind_speed_10m"
    )
    HOURLY_VARIABLES: str = "temperature_2m"
    API_CACHE_TTL_SECONDS: int = 60 * 60

    def __init__(self, forecast_days: int, timezone: str) -> None:
        """Initialize the service with forecast configuration."""
        self.forecast_days: int = forecast_days
        self.timezone: str = timezone

    @staticmethod
    @st.cache_data(ttl=API_CACHE_TTL_SECONDS, show_spinner=False)
    def _get_forecast_cached(params: ForecastParams) -> ForecastData:
        """Return cached forecast results for one hour."""
        return OpenMeteoClient().get_forecast(params)

    def _create_forecast_params(
        self,
        location: DashboardLocation,
    ) -> ForecastParams:
        """Return Open-Meteo forecast params for the app."""
        return {
            "latitude": location["latitude"],
            "longitude": location["longitude"],
            "current": self.CURRENT_VARIABLES,
            "hourly": self.HOURLY_VARIABLES,
            "forecast_days": self.forecast_days,
            "timezone": self.timezone,
        }

    def get_forecast(self, location: DashboardLocation) -> ForecastData:
        """Return current and hourly weather for a dashboard location."""
        forecast: ForecastData = self._get_forecast_cached(
            self._create_forecast_params(location)
        )

        return forecast
