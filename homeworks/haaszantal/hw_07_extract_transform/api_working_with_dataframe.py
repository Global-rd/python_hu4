import requests
import pandas as pd
import numpy as np

URL = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250"

#a 250 legnagyobb market cap-pel rendelkező kriptovaluta letöltése
response = requests.get(url=URL).json()

#az eredményt eltárolása egy dataframe-ben
df = pd.DataFrame(response)

print(df)

print("---------------------")

print(df.dtypes)
print(len(df))

print("---------------------")

#a dataframe egyes oszlopaiban hány üres cella található
print(df.isnull().sum())

print("---------------------")

#betekintés a market_cap oszlop 
all_market_cap = df["market_cap"]
print(all_market_cap)

print("---------------------")

#a teljes dataframe-re vonatkozóan a market_cap összegének meghatározása
total_market_cap_df = df["market_cap"].sum()
print(f"A market_cap összege: {total_market_cap_df}")

print("---------------------")

#új dataframe-ben az első 50 kriptovaluta current_price alapján
top50_df = (df.sort_values("current_price", ascending=False).iloc[0:50])

print(top50_df)

print("---------------------")

#a top50_df price_change_percentage_24h alapján csökkenő sorrendben
top50_df_sort = top50_df.sort_values("price_change_percentage_24h", ascending=False)

print(top50_df_sort)

print("---------------------")

#saját függvénnyel a price_change_percentage_24h értékének vizsgálata
def categorize_change_direction(price_change_percentage_24h):
    if price_change_percentage_24h > 0:
        return "+"
    elif price_change_percentage_24h < 0:
        return "-"
    else:
        return "0"

#a függvény vektorizálása
categorize_change_direction_vectorized = np.vectorize(categorize_change_direction)

#új oszlop a top50_df-ben: change_direction és értékkel feltöltve
top50_df["change_direction"] = categorize_change_direction_vectorized(top50_df["price_change_percentage_24h"])

print(top50_df)

print("---------------------")

#ugyanez nem saját függvénnyel, hanem a pandas / numphy művelettel
top50_df["change_direction"] = np.where(top50_df["price_change_percentage_24h"] > 0, "+",
                                    (np.where(top50_df["price_change_percentage_24h"] < 0, "-", "0")))

print(top50_df)