import streamlit as st
import requests
import pandas as pd
import sqlite3
from datetime import datetime

# # --- ADATBÁZIS INICIALIZÁLÁS (Extra 2) ---
def init_db():
    conn = sqlite3.connect("weather_log.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            country TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_search(city, country, temp, humidity, wind):
    conn = sqlite3.connect("weather_log.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO search_logs (city, country, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (city, country, temp, humidity, wind, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Adatbázis létrehozása az induláskor
init_db()

# --- STREAMLIT OLDAL BEÁLLÍTÁSA ---
st.set_page_config(page_title="Időjárás Dashboard", page_icon="🌤️", layout="wide")

st.title("🌤️ Dinamikus Időjárás Dashboard")
st.markdown("Keresd meg a kívánt település pontos időjárását.")

# --- SIDEBAR / INPUT ---
st.sidebar.header("Keresés")
city_input = st.sidebar.text_input("Város neve:", value="Diósd")

if city_input:
    # Kérjünk le több találatot, hogy válogatni lehessen
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_input}&count=20&language=hu&format=json"
    
    try:
        geo_response = requests.get(geocoding_url).json()
        
        if "results" not in geo_response or len(geo_response["results"]) == 0:
            st.sidebar.warning(f"Nem található '{city_input}' nevű település.")
        else:
            results = geo_response["results"]
            
            # Létrehozunk egy listát a legördülő menühöz, amiben benne van a megye és az ország is
            options = []
            for res in results:
                name = res.get("name", "")
                admin1 = res.get("admin1", "")  # Megye / Régió
                country = res.get("country", "") # Ország
                
                # Összerakjuk az olvasható nevet (ha van megye, azt is beleírjuk)
                full_location = f"{name}"
                if admin1:
                    full_location += f", {admin1}"
                if country:
                    full_location += f" ({country})"
                
                options.append(full_location)
            
            # Legördülő menü az egyezéseknek a Sidebar-on
            selected_option = st.sidebar.selectbox("Talált helyszínek közül válassz:", options)
            
            # Megkeressük a kiválasztott opció indexét, hogy megkapjuk a hozzátartozó lat/lon-t
            selected_index = options.index(selected_option)
            geo_data = results[selected_index]
            
            lat = geo_data["latitude"]
            lon = geo_data["longitude"]
            city_name = geo_data["name"]
            country_name = geo_data.get("country", "Ismeretlen ország")
            
            # Forecast API hívás a kiválasztott pontos koordinátákkal (Aktuális + 7 napos óránkénti előrejelzés az Extra 1-hez)
            forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m&hourly=temperature_2m&timezone=auto"
            forecast_response = requests.get(forecast_url).json()
            
            # Aktuális adatok
            current = forecast_response["current"]
            temp = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            wind_speed = current["wind_speed_10m"]
            
            # --- Extra 2: Logolás az adatbázisba ---
            # Streamlit session_state-et használunk, hogy egy keresés csak egyszer logolódjon, ne minden gombnyomásra/frissítésre            
            log_key = f"{city_name}_{country_name}_{temp}_{humidity}"
            if "last_logged" not in st.session_state or st.session_state.last_logged != log_key:
                log_search(city_name, country_name, temp, humidity, wind_speed)
                st.session_state.last_logged = log_key

            # --- DASHBOARD MEGJELENÍTÉS ---
            st.subheader(f"Aktuális időjárás: {selected_option}")
            
            # Elrendezés Tab-ek segítségével
            tab1, tab2, tab3 = st.tabs(["📊 Aktuális KPI-ok", "📈 Heti Előrejelzés (Grafikon)", "🗄️ Keresési Előzmények (DB Log)"])
            
            with tab1:
                #  KPI-ok megjelenítése oszlopokban
                col1, col2, col3 = st.columns(3)
                col1.metric(label="Hőmérséklet", value=f"{temp} °C")
                col2.metric(label="Páratartalom", value=f"{humidity} %")
                col3.metric(label="Szélsebesség", value=f"{wind_speed} km/h")
            
            with tab2:
                # --- EXTRA 1: Előrejelzés grafikon ---
                st.write("### Hőmérséklet alakulása a következő napokban (óránként)")
                hourly_data = forecast_response["hourly"]
                df_hourly = pd.DataFrame({
                    "Időpont": pd.to_datetime(hourly_data["time"]),
                    "Hőmérséklet (°C)": hourly_data["temperature_2m"]
                })
                df_hourly.set_index("Időpont", inplace=True)
                st.line_chart(df_hourly)
                
            with tab3:
                st.write("### Legutóbbi keresések az SQLite adatbázisból:")
                conn = sqlite3.connect("weather_log.db")
                df_logs = pd.read_sql_query("SELECT city, country, temperature, humidity, wind_speed, timestamp FROM search_logs ORDER BY id DESC LIMIT 10", conn)
                conn.close()
                st.dataframe(df_logs, use_container_width=True)
                
    except requests.exceptions.RequestException as e:
        st.error(f"Hiba történt az API hívás során: {e}")