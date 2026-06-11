import requests
import pandas as pd

# API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters to get top 250 cryptocurrencies by market cap
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
    "sparkline": False
}

# Fetch data from API
response = requests.get(url, params=params)
data = response.json()

# Create dataframe from the fetched data
df = pd.DataFrame(data)

print("=" * 80)
print("FELADAT 1: Üres cellák száma az oszlopokban")
print("=" * 80)
# Task 1: Find and print empty cells in each column
empty_cells = df.isnull().sum()
print(empty_cells)
print()

print("=" * 80)
print("FELADAT 2: Teljes market_cap összege")
print("=" * 80)
# Task 2: Calculate total market_cap
total_market_cap = df["market_cap"].sum()
print(f"Teljes market_cap: ${total_market_cap:,.2f}")
print()

print("=" * 80)
print("FELADAT 3: Top 50 kriptovaluta current_price alapján")
print("=" * 80)
# Task 3: Create top50_df with first 50 cryptocurrencies by current_price
top50_df = df.nlargest(50, "current_price")[["id", "name", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]].reset_index(drop=True)
print(f"Top 50 kriptovaluta (first 10 sorokkal):")
print(top50_df.head(10))
print()

print("=" * 80)
print("FELADAT 4: Top 50 rendezve price_change_percentage_24h szerint (csökkenő)")
print("=" * 80)
# Task 4: Sort top50_df by price_change_percentage_24h in descending order
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)
print(top50_df.head(10))
print()

print("=" * 80)
print("FELADAT 5: change_direction oszlop hozzáadása")
print("=" * 80)
# Task 5: Create change_direction column
def determine_direction(price_change):
    if price_change > 0:
        return "+"
    elif price_change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(determine_direction)
print(top50_df[["name", "symbol", "price_change_percentage_24h", "change_direction"]].head(10))
print()

print("=" * 80)
print("ÖSSZEFOGLALÁS")
print("=" * 80)
print(f"\nTop 50 kriptovaluta direction értékek eloszlása:")
print(top50_df["change_direction"].value_counts())
