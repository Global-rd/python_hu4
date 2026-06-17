import sqlite3
from datetime import datetime
 
import pandas as pd
import requests
import streamlit as st
 
# ----------------------------------------------------------------------
# Oldal alapbeállításai
# ----------------------------------------------------------------------
st.set_page_config(
    page_title="Weather Map & Data Visualization App",
    page_icon="🌤️",
    layout="wide",
)
 
DB_NAME = "weather_log.db"
 
 
# ----------------------------------------------------------------------
# SQLite – adatbázis és tábla létrehozása + logolás (Extra 2.)
# ----------------------------------------------------------------------
def init_db():
    """Létrehozza az adatbázist és a search_log táblát, ha még nem létezik."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS search_log (
            city        TEXT,
            temperature REAL,
            humidity    REAL,
            wind_speed  REAL,
            searched_at TEXT
        )
        """
    )
    conn.commit()
    conn.close()
 
 
def log_search(city, temperature, humidity, wind_speed):
    """Beszúr egy sort a search_log táblába a keresés adataival."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO search_log (city, temperature, humidity, wind_speed, searched_at)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            city,
            temperature,
            humidity,
            wind_speed,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ),
    )
    conn.commit()
    conn.close()
 
 
def read_log():
    """Visszaadja az összes eddigi keresést DataFrame-ként (legújabb felül)."""
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query(
        "SELECT * FROM search_log ORDER BY searched_at DESC", conn
    )
    conn.close()
    return df
 
 
# ----------------------------------------------------------------------
# API hívások
# ----------------------------------------------------------------------
@st.cache_data(ttl=600, show_spinner=False)
def get_coordinates(city_name):
    """Geocoding API: város nevéből lat/lon koordináta + ország."""
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()  # HTTP hiba esetén kivételt dob
    data = resp.json()
 
    results = data.get("results")
    if not results:
        return None  # nincs ilyen nevű város
 
    r = results[0]
    return {
        "name": r["name"],
        "country": r.get("country", "Unknown"),
        "latitude": r["latitude"],
        "longitude": r["longitude"],
    }
 
 
@st.cache_data(ttl=600, show_spinner=False)
def get_weather(lat, lon):
    """Forecast API: aktuális adatok + óránkénti hőmérséklet 5 napra."""
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto",
    }
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
 
 
# ----------------------------------------------------------------------
# Alkalmazás
# ----------------------------------------------------------------------
init_db()
 
st.title("🌤️ Robot Dreams Python – Weather Map & Data Visualization App")
 
city_name = st.text_input("Enter city name", value="Diósd", placeholder="pl. Budapest")
 
if city_name:
    try:
        # 1-2. lépés: városnévből koordináta a geocoding API-val
        location = get_coordinates(city_name)
 
        if location is None:
            st.warning(
                f"Nem található '{city_name}' nevű város. Próbálj meg egy másik nevet!"
            )
        else:
            # 3. lépés: koordinátából időjárási adat a forecast API-val
            weather = get_weather(location["latitude"], location["longitude"])
            current = weather["current"]
 
            temp = current["temperature_2m"]
            humidity = current["relative_humidity_2m"]
            wind = current["wind_speed_10m"]
 
            # Minden városnévhez kötött szöveg dinamikus (ország is)
            st.header(f"Current Weather in {location['name']}, {location['country']}")
 
            # --- KPI-ok / key metric-ek ---
            c1, c2, c3 = st.columns(3)
            c1.metric("Temperature (°C)", f"{temp} °C")
            c2.metric("Humidity (%)", f"{humidity} %")
            c3.metric("Wind Speed (km/h)", f"{wind} km/h")
 
            # --- Logolás csak ÚJ keresésnél (tab-váltás ne duplikáljon) ---
            if st.session_state.get("last_logged_city") != location["name"]:
                log_search(location["name"], temp, humidity, wind)
                st.session_state["last_logged_city"] = location["name"]
 
            # --- Tabok: térkép / előrejelzés / előzmények ---
            tab_map, tab_forecast, tab_history = st.tabs(
                ["🗺️ Weather Map", "📈 Forecast", "🗃️ Search History"]
            )
 
            # 4. lépés: megjelenítés a dashboardon
            with tab_map:
                st.subheader("Weather Map")
                map_df = pd.DataFrame(
                    {"lat": [location["latitude"]], "lon": [location["longitude"]]}
                )
                st.map(map_df, zoom=9)
 
            with tab_forecast:  # Extra 1.
                st.subheader("Hourly Temperature Forecast (Next 5 Days)")
                forecast_df = pd.DataFrame(
                    {
                        "time": pd.to_datetime(weather["hourly"]["time"]),
                        "Temperature (°C)": weather["hourly"]["temperature_2m"],
                    }
                ).set_index("time")
                st.line_chart(forecast_df, height=400)
 
            with tab_history:
                st.subheader("Korábbi keresések (SQLite log)")
                st.dataframe(read_log(), use_container_width=True)
 
    except requests.exceptions.RequestException as e:
        # Bármilyen hálózati / HTTP hiba esetén warning
        st.warning(f"Hiba történt az API-hívás során: {e}")