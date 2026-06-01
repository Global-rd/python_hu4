import requests
import pandas as pd

# =============================================================================
# ADATOK LETÖLTÉSE A COINGECKO API-RÓL
# Endpoint: https://api.coingecko.com/api/v3/coins/markets
# Paraméterek: vs_currency=usd, per_page=250
# =============================================================================

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

print("=" * 60)
print(f"Letöltött kriptovaluták száma: {len(df)}")
print("=" * 60)

# =============================================================================
# 1. FELADAT – Üres cellák száma oszloponként
# =============================================================================

print("\n1. FELADAT – Üres cellák oszloponként:")
print("-" * 40)
null_counts = df.isnull().sum()
print(null_counts.to_string())

# =============================================================================
# 2. FELADAT – market_cap összege
# =============================================================================

print("\n2. FELADAT – Teljes market_cap összeg:")
print("-" * 40)
total_market_cap = df["market_cap"].sum()
print(f"Összes market cap: ${total_market_cap:,.0f}")

# =============================================================================
# 3. FELADAT – Top 50 df current_price alapján
# =============================================================================

top50_df = df.nlargest(50, "current_price").reset_index(drop=True)

print("\n3. FELADAT – Top 50 kriptovaluta current_price alapján:")
print("-" * 40)
print(top50_df[["name", "symbol", "current_price"]].to_string())

# =============================================================================
# 4. FELADAT – Rendezés price_change_percentage_24h alapján csökkenő sorrendben
# =============================================================================

top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False).reset_index(drop=True)

print("\n4. FELADAT – Top 50 rendezve price_change_percentage_24h szerint (csökkenő):")
print("-" * 40)
print(top50_df[["name", "symbol", "current_price", "price_change_percentage_24h"]].to_string())

# =============================================================================
# 5. FELADAT – change_direction oszlop létrehozása
# =============================================================================

def get_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_direction)

print("\n5. FELADAT – Top 50 df change_direction oszloppal:")
print("-" * 40)
print(top50_df[["name", "symbol", "price_change_percentage_24h", "change_direction"]].to_string())

print("\n" + "=" * 60)
print("change_direction értékek megoszlása:")
print(top50_df["change_direction"].value_counts().to_string())
print("=" * 60)