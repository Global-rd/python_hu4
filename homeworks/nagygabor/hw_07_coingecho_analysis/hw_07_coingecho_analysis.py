
import requests
import pandas as pd


# --- EXTRACT: adatok lehúzása a CoinGecko API-ról ---------------------------

URL = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 250,
}

response = requests.get(URL, params=params)
response.raise_for_status()  
data = response.json()

# Eltároljuk  DataFrame-ben
df = pd.DataFrame(data)


# --- 1. feladat: üres cellák száma oszloponként -----------------------------

print("1. Üres cellák száma oszloponként:")
print(df.isnull().sum())
print()

# --- 2. feladat: a teljes market_cap összege --------------------------------

total_market_cap = df["market_cap"].sum()
print("2. Teljes market cap összege:")
print(total_market_cap)
print()

# --- 3. feladat: top50_df, az első 50 coin current_price alapján ------------

top50_df = df.sort_values(by="current_price", ascending=False).head(50).copy()
print("3. top50_df létrehozva (50 sor):", top50_df.shape)
print()


# --- 4. feladat: rendezés price_change_percentage_24h szerint csökkenően -----

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
print("4. top50_df rendezve price_change_percentage_24h szerint (csökkenő).")
print()


# --- 5. feladat: change_direction oszlop ------------------------

def get_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_direction)

print("5. change_direction oszlop hozzáadva. Példa:")
print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]].head(10))