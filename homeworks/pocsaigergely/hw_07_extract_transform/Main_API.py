import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250
}

print("Retrieve data from the CoinGecko API...")
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Successful retrieval!")
else:
    print(f"An error occurred during the API call! Status code: {response.status_code}")
    exit()

#print(data)
#print("///////////////////////////////////")

df = pd.DataFrame(data)

print(df)
print("=======================================")

print("1. Sum of empty cells by column")
print(df.isnull().sum())

print("=======================================")
total_market_cap = df["market_cap"].sum()
print(f"2. Total market cap sum: {total_market_cap:,.2f}")

print("=======================================")
top50_df = df.sort_values(by=
                          "current_price",
                          ascending=False
                          ).iloc[0:50]
print("3. Top 50 by current price table dimensions:", top50_df.shape)

print("=======================================")
top50_df = top50_df.sort_values(by=
                                'price_change_percentage_24h',
                                ascending=False
                                )
print("4. Order by 24h price change percentage (first 5 results)")
print(top50_df[['name', 'current_price', 'price_change_percentage_24h']].head())

print("=======================================")
def direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(direction)

print("5. New column, direction change. (10 results)")
print(top50_df[['name', 'price_change_percentage_24h', 'change_direction']].iloc[20:30])