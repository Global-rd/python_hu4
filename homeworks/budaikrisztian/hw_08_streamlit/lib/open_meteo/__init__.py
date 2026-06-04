"""Open-Meteo API client package."""

from .client import OpenMeteoClient
from .config import OpenMeteoClientConfig
from .types import (
    CityLocation,
    ForecastData,
    ForecastParams,
    GeocodingSearchParams,
)

__all__ = [
    "CityLocation",
    "ForecastData",
    "ForecastParams",
    "GeocodingSearchParams",
    "OpenMeteoClient",
    "OpenMeteoClientConfig",
]
