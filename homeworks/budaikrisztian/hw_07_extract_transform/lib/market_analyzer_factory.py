"""
Factory for cryptocurrency market analyzer objects.
"""

from .coingecko import CoinMarketData
from .market_analyzer import MarketAnalyzer
from .top50_market_analyzer import Top50MarketAnalyzer


class MarketAnalyzerFactory:
    """Create market analyzer objects from market data."""

    def __init__(self, market_data: list[CoinMarketData]) -> None:
        """Initialize the factory with raw market data."""
        self.market_data: list[CoinMarketData] = market_data

    def create_market_analyzer(self) -> MarketAnalyzer:
        """Create a full market analyzer."""
        return MarketAnalyzer(self.market_data)

    def create_top50_market_analyzer(self) -> Top50MarketAnalyzer:
        """Create a top 50 market analyzer by current price."""
        return Top50MarketAnalyzer(self.market_data)
