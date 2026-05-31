"""
Open-Meteo client configuration.
"""


class OpenMeteoClientConfig:
    """Provide Open-Meteo API endpoint URLs."""

    GEOCODING_BASE_URL: str = "https://geocoding-api.open-meteo.com/v1"
    FORECAST_BASE_URL: str = "https://api.open-meteo.com/v1"

    def get_geocoding_search_url(self) -> str:
        """Return the Open-Meteo geocoding search endpoint URL."""
        return f"{self.GEOCODING_BASE_URL}/search"

    def get_forecast_url(self) -> str:
        """Return the Open-Meteo forecast endpoint URL."""
        return f"{self.FORECAST_BASE_URL}/forecast"
