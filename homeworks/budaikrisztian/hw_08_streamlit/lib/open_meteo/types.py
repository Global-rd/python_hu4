"""
TypedDict models for Open-Meteo API responses.
"""

from collections.abc import Sequence
from typing import NotRequired, TypedDict

type QueryParamPrimitive = bool | int | float | str
type QueryParamValue = QueryParamPrimitive | Sequence[QueryParamPrimitive]


class CityLocation(TypedDict):
    """Location item returned by the Open-Meteo geocoding endpoint."""

    # Open-Meteo internal location identifier.
    id: int
    # Display name of the city or settlement.
    name: str
    # Location latitude used by the forecast endpoint.
    latitude: float
    # Location longitude used by the forecast endpoint.
    longitude: float
    # Full country name.
    country: str
    # ISO country code.
    country_code: str
    # First-level administrative region, if returned.
    admin1: NotRequired[str]
    # Local timezone of the location.
    timezone: str


class GeocodingResponse(TypedDict, total=False):
    """Open-Meteo geocoding response wrapper."""

    # Matching locations returned for the search query.
    results: list[CityLocation]
    # API response generation time in milliseconds.
    generationtime_ms: float


class GeocodingSearchParams(TypedDict, total=False):
    """Query parameters for the Open-Meteo geocoding search endpoint."""

    # City name or search text sent to the geocoding endpoint.
    name: str
    # Maximum number of matching locations to return.
    count: int
    # Response language code, for example "en" or "hu".
    language: str
    # Response format, usually "json".
    format: str


class CurrentWeather(TypedDict):
    """Current weather values returned by Open-Meteo."""

    # Timestamp of the current weather values.
    time: str
    # Measurement interval in seconds.
    interval: int
    # Air temperature at 2 meters above ground in Celsius.
    temperature_2m: float
    # Relative humidity at 2 meters above ground in percent.
    relative_humidity_2m: int
    # Wind speed at 10 meters above ground in km/h.
    wind_speed_10m: float


class HourlyWeather(TypedDict):
    """Hourly forecast values returned by Open-Meteo."""

    # Hourly forecast timestamps.
    time: list[str]
    # Hourly air temperature values at 2 meters above ground in Celsius.
    temperature_2m: list[float]


class ForecastData(TypedDict):
    """Forecast response returned by the Open-Meteo forecast endpoint."""

    # Forecast latitude, usually adjusted to the nearest weather grid point.
    latitude: float
    # Forecast longitude, usually adjusted to the nearest weather grid point.
    longitude: float
    # Timezone used for current and hourly timestamps.
    timezone: str
    # Current weather values requested with the current query parameter.
    current: CurrentWeather
    # Hourly weather values requested with the hourly query parameter.
    hourly: HourlyWeather


class ForecastParams(TypedDict, total=False):
    """Query parameters for the Open-Meteo forecast endpoint."""

    # Location latitude from geocoding or another location source.
    latitude: float
    # Location longitude from geocoding or another location source.
    longitude: float
    # Comma-separated current weather variables to request.
    current: str
    # Comma-separated hourly weather variables to request.
    hourly: str
    # Number of forecast days to return.
    forecast_days: int
    # Forecast timezone handling, for example "auto".
    timezone: str
