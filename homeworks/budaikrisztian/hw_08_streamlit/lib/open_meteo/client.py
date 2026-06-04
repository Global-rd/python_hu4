"""
Open-Meteo API client for geocoding and weather forecasts.
"""

import json
from typing import cast

import requests

from .config import OpenMeteoClientConfig
from .types import (
    CityLocation,
    ForecastData,
    ForecastParams,
    GeocodingResponse,
    GeocodingSearchParams,
    QueryParamValue,
)


class OpenMeteoClient:
    """Fetch location and weather data from the Open-Meteo public APIs."""

    def __init__(
        self,
        config: OpenMeteoClientConfig | None = None,
        timeout: int = 30,
    ) -> None:
        """Initialize the client with Open-Meteo endpoint URLs."""
        self.config: OpenMeteoClientConfig = config or OpenMeteoClientConfig()
        self.timeout: int = timeout
        self.geocoding_search_url: str = (
            self.config.get_geocoding_search_url()
        )
        self.forecast_url: str = self.config.get_forecast_url()

    def __get_json(
        self,
        url: str,
        params: dict[str, QueryParamValue],
    ) -> object:
        """Send a GET request and return the decoded JSON response."""
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise RuntimeError(
                f"Open-Meteo API request failed: {error}"
            ) from error
        except json.JSONDecodeError as error:
            raise RuntimeError(
                "Open-Meteo API response is not valid JSON."
            ) from error
        except Exception as error:
            raise RuntimeError(
                f"Unexpected Open-Meteo API error: {error}"
            ) from error

    def search_cities(
        self,
        params: GeocodingSearchParams,
    ) -> list[CityLocation]:
        """Return matching locations from the geocoding search endpoint."""
        request_params: dict[str, QueryParamValue] = {
            key: cast(QueryParamValue, value) for key, value in params.items()
        }

        if "name" not in request_params:
            raise ValueError("Missing required Open-Meteo param: name")

        response_data = cast(
            GeocodingResponse,
            self.__get_json(self.geocoding_search_url, request_params),
        )

        return response_data.get("results", [])

    def get_forecast(self, params: ForecastParams) -> ForecastData:
        """Return current weather and hourly forecast."""
        request_params: dict[str, QueryParamValue] = {
            key: cast(QueryParamValue, value) for key, value in params.items()
        }

        if "latitude" not in request_params:
            raise ValueError("Missing required Open-Meteo param: latitude")

        if "longitude" not in request_params:
            raise ValueError("Missing required Open-Meteo param: longitude")

        response_data = self.__get_json(self.forecast_url, request_params)

        return cast(ForecastData, response_data)
