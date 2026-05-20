"""
TypedDict models for CoinGecko API responses.
"""

from collections.abc import Sequence
from typing import Literal, NotRequired, TypedDict

type Number = int | float
type QueryParamPrimitive = bool | int | float | str
type QueryParamValue = QueryParamPrimitive | Sequence[QueryParamPrimitive]
type IncludeTokens = Literal["top", "all"]
type MarketOrder = Literal[
    "market_cap_asc",
    "market_cap_desc",
    "volume_asc",
    "volume_desc",
    "id_asc",
    "id_desc",
]
type PricePrecision = Literal[
    "full",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
]
type Locale = Literal[
    "ar",
    "bg",
    "cs",
    "da",
    "de",
    "el",
    "en",
    "es",
    "fi",
    "fr",
    "he",
    "hi",
    "hr",
    "hu",
    "id",
    "it",
    "ja",
    "ko",
    "lt",
    "nl",
    "no",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "sv",
    "th",
    "tr",
    "uk",
    "vi",
    "zh",
    "zh-tw",
]


class CoinMarketsParams(TypedDict, total=False):
    """Query parameters for the CoinGecko coins markets endpoint."""

    # Target currency for price and market data.
    vs_currency: str
    # Coin IDs, comma-separated.
    ids: str
    # Coin names, comma-separated.
    names: str
    # Coin symbols, comma-separated.
    symbols: str
    # Token match behavior when symbols are used.
    include_tokens: IncludeTokens
    # Coin category filter.
    category: str
    # Result ordering.
    order: MarketOrder
    # Number of results per page. Valid range: 1..250.
    per_page: int
    # Page number.
    page: int
    # Include 7-day sparkline data.
    sparkline: bool
    # Price change timeframes, comma-separated.
    price_change_percentage: str
    # Response localization.
    locale: Locale
    # Price decimal precision.
    precision: PricePrecision
    # Include rehypothecated token data.
    include_rehypothecated: bool


class RoiData(TypedDict):
    """Return on investment data from CoinGecko."""

    # Multiplier compared to the initial investment.
    times: Number | None
    # Currency used for the ROI calculation.
    currency: str
    # ROI percentage value.
    percentage: Number | None


class CoinMarketData(TypedDict):
    """Coin market data returned by the CoinGecko markets endpoint."""

    # CoinGecko coin identifier.
    id: str
    # Short trading symbol.
    symbol: str
    # Display name of the coin.
    name: str
    # URL of the coin icon image.
    image: str
    # Latest price in the selected vs_currency.
    current_price: Number | None
    # Current market capitalization.
    market_cap: Number | None
    # Market cap ranking.
    market_cap_rank: Number | None
    # Optional market cap rank with rehypothecated assets included.
    market_cap_rank_with_rehypothecated: NotRequired[Number | None]
    # Valuation if the maximum supply were fully circulating.
    fully_diluted_valuation: Number | None
    # Trading volume over the last 24 hours.
    total_volume: Number | None
    # Highest price over the last 24 hours.
    high_24h: Number | None
    # Lowest price over the last 24 hours.
    low_24h: Number | None
    # Absolute price change over the last 24 hours.
    price_change_24h: Number | None
    # Percentage price change over the last 24 hours.
    price_change_percentage_24h: Number | None
    # Absolute market cap change over the last 24 hours.
    market_cap_change_24h: Number | None
    # Percentage market cap change over the last 24 hours.
    market_cap_change_percentage_24h: Number | None
    # Number of coins currently circulating.
    circulating_supply: Number | None
    # Total created or available supply.
    total_supply: Number | None
    # Maximum possible supply.
    max_supply: Number | None
    # All-time high price.
    ath: Number | None
    # Percentage change from the all-time high.
    ath_change_percentage: Number | None
    # Date of the all-time high.
    ath_date: str | None
    # All-time low price.
    atl: Number | None
    # Percentage change from the all-time low.
    atl_change_percentage: Number | None
    # Date of the all-time low.
    atl_date: str | None
    # Return on investment data, if available.
    roi: RoiData | None
    # Last update timestamp from CoinGecko.
    last_updated: str
