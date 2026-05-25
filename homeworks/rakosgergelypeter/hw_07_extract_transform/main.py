
from api import CoinGeckoAPIClient
from gecko_analyzer import CryptoDataAnalyzer

class Application:

    def run(self):
        api_client = CoinGeckoAPIClient()
        data = api_client.get_market_data()
        analyzer = CryptoDataAnalyzer(data)
        analyzer.run_analysis()

if __name__ == "__main__":
    app = Application()
    app.run()