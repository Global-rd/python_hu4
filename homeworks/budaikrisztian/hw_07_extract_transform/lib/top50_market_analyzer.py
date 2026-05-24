"""
Pandas transformations for the top 50 cryptocurrency dataframe.
"""

import numpy as np
import pandas as pd

from .coingecko import CoinMarketData


class Top50MarketAnalyzer:
    """Analyze and transform the top 50 cryptocurrency dataframe."""

    def __init__(self, market_data: list[CoinMarketData]) -> None:
        """Initialize the analyzer with the top 50 dataframe."""
        self.top50_df: pd.DataFrame = (
            pd.DataFrame(market_data)
            .sort_values("current_price", ascending=False)
            .head(50)
        )

    def sort_by_24h_change(self) -> pd.DataFrame:
        """Sort top50_df by 24-hour price change percentage descending."""
        self.top50_df = self.top50_df.sort_values(
            "price_change_percentage_24h",
            ascending=False,
        )

        return self.top50_df

    def add_change_direction_column(self) -> pd.DataFrame:
        """Add the change_direction column to top50_df."""
        price_change = self.top50_df["price_change_percentage_24h"]
        self.top50_df["change_direction"] = np.select(
            [
                price_change > 0,
                price_change < 0,
            ],
            [
                "+",
                "-",
            ],
            default="0",
        )

        return self.top50_df
