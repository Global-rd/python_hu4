# solution.py
# 7. hazi feladat - CoinGecko API + Pandas adattranszformacio

import requests
import pandas as pd
import numpy as np

# ============================================================
# 1. ADATKINYERES - CoinGecko API
# ============================================================
URL = "https://api.coingecko.com/api/v3/coins/markets"

# 2 parametert hasznalunk az API dokumentacio szerint:
# - vs_currency: kotelezo, milyen penznemben kerjuk az arakat
# - per_page: hany eredmenyt kerunk (max 250)
# Az alapertelmezett rendezes market_cap_desc, tehat
# automatikusan a legnagyobb market cap-tol indul.
params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(URL, params=params)

# Ellenorzes: sikeres volt-e a kérés
if response.status_code != 200:
    print(f"Hiba a request soran! Status code: {response.status_code}")
    exit()

# JSON string -> Python list of dictionaries
data = response.json()

# List of dictionaries -> DataFrame (14. oran tanult mintaval)
df = pd.DataFrame(data)

print(f"DataFrame merete: {df.shape}")
print(f"Sorok szama: {len(df)}\n")


# ============================================================
# 1. FELADAT: Ures cellak szama oszloponkent
# ============================================================
print("=" * 60)
print("1. FELADAT: Ures cellak szama oszloponkent")
print("=" * 60)
print(df.isnull().sum())
print()


# ============================================================
# 2. FELADAT: Teljes market_cap osszege
# ============================================================
print("=" * 60)
print("2. FELADAT: Teljes market_cap osszege")
print("=" * 60)
total_market_cap = df["market_cap"].sum()
print(f"Total market cap: ${total_market_cap:,.2f}")
print()


# ============================================================
# 3. FELADAT: Top 50 DataFrame current_price alapjan
# ============================================================
print("=" * 60)
print("3. FELADAT: Top 50 DataFrame current_price alapjan")
print("=" * 60)
top50_df = df.sort_values(by="current_price", ascending=False).head(50)
print(top50_df[["name", "current_price"]])
print()


# ============================================================
# 4. FELADAT: top50_df rendezve price_change_percentage_24h szerint
# ============================================================
print("=" * 60)
print("4. FELADAT: top50_df rendezve price_change_percentage_24h szerint")
print("=" * 60)
top50_df = top50_df.sort_values(
    by="price_change_percentage_24h",
    ascending=False
)
print(top50_df[["name", "price_change_percentage_24h"]])
print()


# ============================================================
# 5. FELADAT: change_direction oszlop letrehozasa
# (vektorizalt megoldas, 14. oran tanult np.select-tel)
# ============================================================
print("=" * 60)
print("5. FELADAT: change_direction oszlop")
print("=" * 60)

conditions = [
    top50_df["price_change_percentage_24h"] > 0,
    top50_df["price_change_percentage_24h"] < 0,
    top50_df["price_change_percentage_24h"] == 0,
]
choices = ["+", "-", "0"]

top50_df["change_direction"] = np.select(conditions, choices, default="0")

print(top50_df[["name", "price_change_percentage_24h", "change_direction"]])