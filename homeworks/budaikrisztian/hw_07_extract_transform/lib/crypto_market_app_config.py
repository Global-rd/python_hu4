"""
Application-level configuration for the cryptocurrency market analysis.
"""

import os

from dotenv import load_dotenv

from .coingecko import CoinGeckoClientConfig, CoinMarketsParams


class CryptoMarketAppConfig:
    """Provide application-level CoinGecko query defaults."""

    DEFAULT_VS_CURRENCY: str = "usd"
    DEFAULT_MARKET_PER_PAGE: int = 250

    def __init__(self) -> None:
        """Load the local dotenv file and read app-level settings."""
        load_dotenv(dotenv_path=CoinGeckoClientConfig.ENV_FILE_PATH)
        self.vs_currency: str = os.environ.get(
            "CRYPTO_MARKET_VS_CURRENCY",
            self.DEFAULT_VS_CURRENCY,
        )
        self.market_per_page: str = os.environ.get(
            "CRYPTO_MARKET_PER_PAGE",
            str(self.DEFAULT_MARKET_PER_PAGE),
        )

    def get_vs_currency(self) -> str:
        """Return the configured market target currency."""
        return self.vs_currency.strip().lower()

    def get_market_per_page(self) -> int:
        """Return the configured market result limit."""
        try:
            market_per_page: int = int(self.market_per_page)
        except ValueError as error:
            raise ValueError(
                "CRYPTO_MARKET_PER_PAGE must be an integer."
            ) from error

        if market_per_page < 1 or market_per_page > 250:
            raise ValueError(
                "CRYPTO_MARKET_PER_PAGE must be between 1 and 250."
            )

        return market_per_page

    def get_market_params(self) -> CoinMarketsParams:
        """Return query params for the homework market data request."""
        return {
            "vs_currency": self.get_vs_currency(),
            "per_page": self.get_market_per_page(),
        }
