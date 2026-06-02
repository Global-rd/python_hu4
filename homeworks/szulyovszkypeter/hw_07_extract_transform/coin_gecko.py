import requests
import pandas as pd
import numpy as np

# Az API végpont és a két kért paraméter beállítása
URL = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # célvaluta
    "per_page": 250        # a 250 legnagyobb market cap-pel rendelkező coin
}

print("Adatok lekérése a CoinGecko API-ról...")
response = requests.get(URL, params=params)

if response.status_code == 200:
    data = response.json()
    # Adatok betöltése a DataFrame-be
    df = pd.DataFrame(data)
    print(f"Sikeres lekérés! {len(df)} kriptovaluta adata beöltve.\n")
 # -------------------------------------------------------------------------
    # 1. Feladat: Üres cellák meghatározása oszloponként és kinyomtatása
    # -------------------------------------------------------------------------
    print("1. Üres cellák száma az egyes oszlopokban:")
    missing_values = df.isnull().sum()
    print()
    print(missing_values)
    print("-" * 60)
   
    # -------------------------------------------------------------------------
    # 2. Feladat: A teljes dataframe-re a market_cap összegének meghatározása
    # -------------------------------------------------------------------------
    total_market_cap = df["market_cap"].sum()
    print(f"2. A teljes df market_cap összege: {total_market_cap:,.2f} USD")
    print("-" * 60)
       
    # -------------------------------------------------------------------------
    # 3. Feladat: Új top50_df létrehozása a current_price alapján (első 50)
    # -------------------------------------------------------------------------
    # A nlargest() függvény kiválasztja a legnagyobb értékű elemeket az adott oszlopból
    top50_df = df.nlargest(50, "current_price").copy()
    print(f"3. top50_df sikeresen létrehozva. Sorok száma: {len(top50_df)} (a legmagasabb árú coinok)")
    print()
    print(top50_df[["name", "current_price", "price_change_percentage_24h"]].head(10))
    print("-" * 60)
    
    # -------------------------------------------------------------------------
    # 4. Feladat: A top50_df rendezése price_change_percentage_24h alapján csökkenőbe
    # -------------------------------------------------------------------------
    top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
    print("4. top50_df rendezve price_change_percentage_24h alapján csökkenő sorrendbe.")
    print()
    print(top50_df[["name", "current_price", "price_change_percentage_24h"]].head(10))
    print("-" * 60)
    
    # -------------------------------------------------------------------------
    # 5. Feladat: Új change_direction oszlop létrehozása az alábbi feltételek szerint
        #a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
        #b. Ha negatív, az oszlop értéke legyen “-“
        #c. Ha kereken 0, az érték legyen “0”
    # -------------------------------------------------------------------------
    # Feltételek definiálása
    conditions = [
        top50_df["price_change_percentage_24h"] > 0,
        top50_df["price_change_percentage_24h"] < 0,
        top50_df["price_change_percentage_24h"] == 0
    ]
    # A feltételekhez tartozó értékek meghatározása
    choices = ["+", "-", "0"]
    
    # Az np.select segítségével hatékonyan kitölthetjük az új oszlopot
    top50_df["change_direction"] = np.select(conditions, choices, default=None)
    
    print("5. A 'change_direction' oszlop hozzáadva a feltételek alapján.")
    print("=" * 60)
    
    # Betekintés az elkészült top50_df eredményébe (első néhány sor)
    print("A rendezett és módosított top50_df első 10 sorra:")
    print()
    print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]].head(10))
else:
    print(f"Hiba történt az API hívás során! Státuszkód: {response.status_code}")
    print("Próbáld meg kicsit később, hátha valami limibe futottam (rate limit).")
    