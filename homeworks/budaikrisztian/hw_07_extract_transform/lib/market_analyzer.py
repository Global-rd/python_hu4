"""
Pandas transformations for cryptocurrency market data.
"""

import pandas as pd

from .coingecko import CoinMarketData


class MarketAnalyzer:
    """Analyze cryptocurrency market data stored in a dataframe."""

    def __init__(self, market_data: list[CoinMarketData]) -> None:
        """Initialize the analyzer with raw market data."""
        self.df: pd.DataFrame = pd.DataFrame(market_data)

    def get_empty_cell_counts(self) -> pd.Series:
        """Return the number of empty cells in every dataframe column."""
        return self.df.isna().sum()

    def get_total_market_cap(self) -> float:
        """Return the total market cap of the full dataframe."""
        return self.df["market_cap"].sum()
