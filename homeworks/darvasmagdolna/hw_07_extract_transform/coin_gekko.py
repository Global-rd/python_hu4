import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = { 
    "vs_currency": "USD",
    "order": "market_cap_rank",
    "per_page": 250,
    "page": 1

}

response = requests.get(url, params=params)
data = response.json()

dataFrame = pd.DataFrame(data)
print("Number of empty cells per column: ")
print(dataFrame.isna().sum())

# 2 feladat

total_market_cap = dataFrame["market_cap"].sum()
print(f"\nTotal Market Cap: {total_market_cap}")

# 3 feladat

top50_df = dataFrame.sort_values("current_price", ascending=False).head(50)

# 4 feladat

top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5 feladat

def direction(x):
    if x > 0:
        return "+"
    elif x < 0:
        return "-"
    else:
        return "0"
    
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(direction)

print("\nTop 50:")
print(top50_df[["id", "current_price", "price_change_percentage_24h"]].head())



 
    

