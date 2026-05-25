import requests
import pandas as pd
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency" : "usd",
    "per_page" : 250
}
response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data)

print("Number of empty cells per columns")
print(df.isnull().sum())

total_market_cap = df["market_cap"].sum()
print(f"Total market cap: {total_market_cap} USD")

top50_df = (
    df.sort_values(by="current_price", ascending=False)
    .head(50)
    .copy()
)

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

top50_df["change_direction"] = np.where(
    top50_df["price_change_percentage_24h"] > 0, "+",
     np.where(
    top50_df["price_change_percentage_24h"] < 0, "-", "0"   
     ))
