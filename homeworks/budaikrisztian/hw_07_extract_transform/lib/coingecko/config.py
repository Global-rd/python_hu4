"""
CoinGecko client configuration loaded from dotenv.
"""

import os
from pathlib import Path

from dotenv import load_dotenv


class CoinGeckoClientConfig:
    """Load and provide CoinGecko client configuration."""

    DEMO_API_MODE: str = "demo"
    PRO_API_MODE: str = "pro"
    DEMO_BASE_URL: str = "https://api.coingecko.com/api/v3"
    PRO_BASE_URL: str = "https://pro-api.coingecko.com/api/v3"
    DEMO_API_KEY_HEADER_NAME: str = "x-cg-demo-api-key"
    PRO_API_KEY_HEADER_NAME: str = "x-cg-pro-api-key"
    ENV_FILE_PATH: Path = Path(__file__).parent.parent.parent / ".env"

    def __init__(self) -> None:
        """Load the local dotenv file and read CoinGecko settings."""
        load_dotenv(dotenv_path=self.ENV_FILE_PATH)
        self.api_mode: str = os.environ.get(
            "COINGECKO_API_MODE",
            self.DEMO_API_MODE,
        )
        self.api_key: str = os.environ.get("COINGECKO_API_KEY", "")

    def get_api_mode(self) -> str:
        """Return the configured CoinGecko API mode."""
        api_mode: str = self.api_mode.strip().lower()

        if api_mode not in (self.DEMO_API_MODE, self.PRO_API_MODE):
            raise ValueError(
                f"Unsupported CoinGecko API mode: {api_mode}. "
                f"Supported values: {self.DEMO_API_MODE}, "
                f"{self.PRO_API_MODE}"
            )

        return api_mode

    def get_base_url(self) -> str:
        """Return the configured CoinGecko base URL."""
        if self.get_api_mode() == self.PRO_API_MODE:
            return self.PRO_BASE_URL

        return self.DEMO_BASE_URL

    def get_markets_url(self) -> str:
        """Return the CoinGecko coins markets endpoint URL."""
        return f"{self.get_base_url()}/coins/markets"

    def get_supported_vs_currencies_url(self) -> str:
        """Return the CoinGecko supported currencies endpoint URL."""
        return f"{self.get_base_url()}/simple/supported_vs_currencies"

    def get_api_key_header_name(self) -> str:
        """Return the configured CoinGecko API key header name."""
        if self.get_api_mode() == self.PRO_API_MODE:
            return self.PRO_API_KEY_HEADER_NAME

        return self.DEMO_API_KEY_HEADER_NAME

    def get_headers(self) -> dict[str, str]:
        """Return request headers for the CoinGecko API."""
        if self.api_key == "":
            return {}

        return {self.get_api_key_header_name(): self.api_key}
