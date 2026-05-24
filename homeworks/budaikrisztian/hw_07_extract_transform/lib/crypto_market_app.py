"""
Main cryptocurrency market analysis application class.
"""

from .coingecko import CoinGeckoClient, CoinGeckoClientConfig, CoinMarketData
from .crypto_market_app_config import CryptoMarketAppConfig
from .market_analyzer_factory import MarketAnalyzerFactory


class CryptoMarketApp:
    """Run the cryptocurrency market analysis flow."""

    SECTION_SEPARATOR: str = f"\n{'=' * 80}\n"

    def __init__(
        self,
        coingecko_config: CoinGeckoClientConfig,
        app_config: CryptoMarketAppConfig,
    ) -> None:
        """Initialize the application dependencies."""
        self.client: CoinGeckoClient = CoinGeckoClient(coingecko_config)
        self.app_config: CryptoMarketAppConfig = app_config

    @staticmethod
    def display_top50_columns() -> list[str]:
        """Return the columns displayed from top50_df."""
        return [
            "name",
            "symbol",
            "current_price",
            "price_change_percentage_24h",
            "change_direction",
        ]

    def run(self) -> None:
        """Run the complete extract and transform flow."""
        market_data: list[CoinMarketData] = self.client.get_coin_markets(
            self.app_config.get_market_params()
        )
        analyzer_factory = MarketAnalyzerFactory(market_data)
        analyzer = analyzer_factory.create_market_analyzer()

        print(self.SECTION_SEPARATOR)
        print("Empty cell counts by column:")
        print(analyzer.get_empty_cell_counts())

        print(self.SECTION_SEPARATOR)
        print("Total market cap:")
        print(analyzer.get_total_market_cap())

        top50_analyzer = analyzer_factory.create_top50_market_analyzer()
        top50_analyzer.sort_by_24h_change()
        top50_df = top50_analyzer.add_change_direction_column()

        print(self.SECTION_SEPARATOR)
        print("Top 50 cryptocurrencies by current price:")
        print(top50_df[self.display_top50_columns()])
