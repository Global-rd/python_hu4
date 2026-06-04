import requests
import pandas as pd

# 1. API hívás
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

# DataFrame létrehozása
df = pd.DataFrame(data)

# 1. feladat – üres cellák száma oszloponként
print("Üres cellák oszloponként:")
print(df.isna().sum())

# 2. feladat – market_cap összegzése
total_market_cap = df["market_cap"].sum()
print("\nA teljes market_cap összege:", total_market_cap)

# 3. feladat – top50_df current_price alapján
top50_df = df.sort_values("current_price", ascending=False).head(50)

# 4. feladat – rendezés price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5. feladat – új oszlop: change_direction
def direction(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(direction)

print("\nA top50_df első 5 sora:")
print(top50_df.head())
