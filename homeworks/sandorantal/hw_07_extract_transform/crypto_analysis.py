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

df = pd.DataFrame(data)

print("\n--- Task 1: Number of empty cells per column ---")
missing_values = df.isnull().sum()
print(missing_values)


print("\n--- Task 2: Total market_cap amount ---")
total_market_cap = df['market_cap'].sum()
print(f"Total market capitalization of the top 250 cryptocurrencies: ${total_market_cap:,.2f}")


print("\n--- Task 3: Create a Top 50 DataFrame based on current_price ---")

top50_df = df.sort_values(by='current_price', ascending=False).head(50).copy()
print(f"A top50_df sikeresen létrehozva. Sorok száma: {len(top50_df)}")


print("\n--- Task 4: Sort Top 50 by price_change_percentage_24h ---")
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)
print(top50_df[['name', 'current_price', 'price_change_percentage_24h']].head())


print("\n--- Task 5: Create a change_direction column ---")
def get_direction(percentage):
    if percentage > 0:
        return "+"
    elif percentage < 0:
        return "-"
    else:
        return "0"

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(get_direction)

print(top50_df[['name', 'price_change_percentage_24h', 'change_direction']].head(10))