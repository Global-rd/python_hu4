"""
CoinGecko API client for market data extraction.
"""

import json
from typing import cast

import requests

from .config import CoinGeckoClientConfig
from .types import (
    CoinMarketData,
    CoinMarketsParams,
    QueryParamValue,
)


class CoinGeckoClient:
    """Fetch cryptocurrency market data from the CoinGecko public API."""

    def __init__(
        self,
        config: CoinGeckoClientConfig | None = None,
        timeout: int = 30,
    ) -> None:
        """Initialize the client with the coins markets endpoint."""
        self.config: CoinGeckoClientConfig = config or CoinGeckoClientConfig()
        self.timeout: int = timeout
        self.markets_url: str = self.config.get_markets_url()
        self.supported_vs_currencies_url: str = (
            self.config.get_supported_vs_currencies_url()
        )
        self.supported_vs_currencies: list[str] = []

    def __get_json(
        self,
        url: str,
        params: dict[str, QueryParamValue] | None = None,
    ) -> object:
        """Send a GET request and return the JSON response."""
        try:
            response = requests.get(
                url,
                params=params,
                headers=self.config.get_headers(),
                timeout=self.timeout,
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as error:
            raise RuntimeError(
                f"CoinGecko API request failed: {error}"
            ) from error
        except json.JSONDecodeError as error:
            raise RuntimeError(
                "CoinGecko API response is not valid JSON."
            ) from error
        except Exception as error:
            raise RuntimeError(
                f"Unexpected CoinGecko API error: {error}"
            ) from error

    def get_supported_vs_currencies(self) -> list[str]:
        """Return the currencies supported by CoinGecko."""
        if len(self.supported_vs_currencies) > 0:
            return self.supported_vs_currencies

        response_data = self.__get_json(self.supported_vs_currencies_url)
        self.supported_vs_currencies = cast(list[str], response_data)

        return self.supported_vs_currencies

    def validate_vs_currency(self, vs_currency: str) -> str:
        """Return the configured currency if CoinGecko supports it."""
        normalized_vs_currency: str = vs_currency.strip().lower()
        supported_currencies: list[str] = self.get_supported_vs_currencies()

        if normalized_vs_currency not in supported_currencies:
            raise ValueError(
                "Unsupported CoinGecko vs_currency: "
                f"{normalized_vs_currency}. "
                f"Supported values: {', '.join(supported_currencies)}"
            )

        return normalized_vs_currency

    def get_coin_markets(
        self,
        params: CoinMarketsParams,
    ) -> list[CoinMarketData]:
        """Return coin market data from the coins markets endpoint."""
        request_params: dict[str, QueryParamValue] = {
            key: cast(QueryParamValue, value) for key, value in params.items()
        }

        if "vs_currency" not in request_params:
            raise ValueError("Missing required CoinGecko param: vs_currency")

        request_params["vs_currency"] = self.validate_vs_currency(
            str(request_params["vs_currency"])
        )
        response_data = self.__get_json(self.markets_url, request_params)

        return cast(list[CoinMarketData], response_data)
