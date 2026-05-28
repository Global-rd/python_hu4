# IMPORTS
import requests
import pandas as pd

# CONSTANTS
COINGECKO_URL = 'https://api.coingecko.com/api/v3/coins/markets'
DEFAULT_CURR = 'usd'
DEFAULT_PAGE = '250'

# CLASS
class CoinGecko:
    def __init__(self, vs_currency = DEFAULT_CURR, per_page = DEFAULT_PAGE):
        self.url = COINGECKO_URL
        self.parameters = {
            'vs_currency': vs_currency,
            'per_page': per_page
        }
        self.df = None
        self.df_top_50 = None


    def make_df(self) -> None:
        api_response = requests.get(self.url, params = self.parameters)
        self.df = pd.DataFrame(api_response.json())
        print(self.df)


    def count_none_datas(self) -> None:
        print('üres cellák...')
        print(self.df.isnull().sum())


    def sum_market_cap(self) -> None:
        print('Summa:')
        print(self.df['market_cap'].sum())


    def top_50_market_cap(self) -> None:
        self.top_50_df = self.df.sort_values(
            by = 'current_price',
            ascending = False
        ).iloc[0:50]


    def top_50_sorted_market_cap(self) -> None:
        self.top_50_sorted = self.top_50_df.sort_values(
            by = 'price_change_percentage_24h',
            ascending = False
        )


    def make_change_direction_coloumn(self) -> None:

        def switch_direction(direction):
            if direction > 0:
                return '+'
            elif direction < 0:
                return '-'
            else:
                return '0'

        self.top_50_df['change direction'] = self.top_50_df[
            'price_change_percentage_24h'
        ].apply(switch_direction)


# CODE
def main():
    hw_07 = CoinGecko()

    hw_07.make_df()
    hw_07.count_none_datas()
    hw_07.sum_market_cap()
    hw_07.top_50_market_cap()
    hw_07.top_50_sorted_market_cap()
    hw_07.make_change_direction_coloumn()

    print(hw_07.top_50_df.head(10))


# CODE RUNNER
if __name__ == '__main__':
    main()