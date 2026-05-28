import requests

class CoinGeckoAPIClient:

    BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"

    def __init__(self, currency: str="usd", per_page: int=250):

        self.currency = currency
        self.per_page = per_page

    def get_market_data(self) -> list:

        params = {
            "vs_currency": self.currency,
            "per_page": self.per_page
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:

            raise Exception(f"API error: {response.status_code}, {response.text}")

        return response.json()