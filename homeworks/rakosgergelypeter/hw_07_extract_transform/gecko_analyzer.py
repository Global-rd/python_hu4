import pandas as pd

class CryptoDataAnalyzer:

    def __init__(self, data: list):

        self.df = pd.DataFrame(data)

    def null_values(self):

        print(self.df.isnull().sum())

    def sum_market_cap(self):

        total_market_cap = self.df["market_cap"].sum()
        print(total_market_cap)

    def create_top50_by_current_price(self) -> pd.DataFrame:

        top50_df = self.df.sort_values(
            by="current_price",
            ascending=False
        ).head(50)

        return top50_df

    def order_top50_by_24h_change(self, top50_df: pd.DataFrame) -> pd.DataFrame:

        top50_df = top50_df.sort_values(
            by="price_change_percentage_24h",
            ascending=False
        )

        return top50_df

    def add_change_direction_column(self, top50_df: pd.DataFrame) -> pd.DataFrame:
        
        def determine_direction(value):

            if value > 0:

                return "+"

            elif value < 0:

                return "-"

            else:

                return "0"

        top50_df["change_direction"] = top50_df[
            "price_change_percentage_24h"
        ].apply(determine_direction)

        return top50_df

    def run_analysis(self):

        print("1. Null oszlopok:")
        self.null_values()
        print("2. Összesített market cap:")
        self.sum_market_cap()
        top50_df = self.create_top50_by_current_price()
        top50_df = self.order_top50_by_24h_change(top50_df)
        top50_df = self.add_change_direction_column(top50_df)

        print("\n3-5. top50_df eredmény:")
        print(
            top50_df[
                [
                    "id",
                    "symbol",
                    "name",
                    "current_price",
                    "market_cap",
                    "price_change_percentage_24h",
                    "change_direction"
                ]
            ]
        )