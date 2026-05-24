"""
Homework 7: Extract and transform cryptocurrency market data.
Author: Budai Krisztian
"""

from lib.coingecko import CoinGeckoClientConfig
from lib.crypto_market_app import CryptoMarketApp
from lib.crypto_market_app_config import CryptoMarketAppConfig

if __name__ == "__main__":
    coingecko_config = CoinGeckoClientConfig()
    app_config = CryptoMarketAppConfig()

    CryptoMarketApp(coingecko_config, app_config).run()
