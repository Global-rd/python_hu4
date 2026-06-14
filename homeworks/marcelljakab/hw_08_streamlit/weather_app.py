import sqlite3
from datetime import datetime

import pandas as pd
import plotly.express as px
import requests
import streamlit as st

from db_logger import SQLiteDB

# --- Konstansok ---
GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
DB_NAME = "weather_logs.db"


@st.cache_data(ttl=600)
def get_coordinates(city_name):
    """A városnévhez lekéri a lat/lon-t és az országot a geocoding API-ról."""
    params = {"name": city_name, "count": 1, "language": "hu", "format": "json"}
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if "results" not in data:
        return None
    top = data["results"][0]
    return {
        "name": top["name"],
        "country": top.get("country", "Ismeretlen"),
        "lat": top["latitude"],
        "lon": top["longitude"],
    }


@st.cache_data(ttl=600)
def get_weather(lat, lon):
    """A koordinátákhoz lekéri a jelenlegi időjárást és az 5 napos előrejelzést."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "forecast_days": 5,
        "timezone": "auto",
    }
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code != 200:
        return None
    return response.json()


def log_search(city, temperature, humidity, wind_speed):
    """Eltárol egy keresést az adatbázisban: város, 3 mérőszám és az időpont."""
    with SQLiteDB(DB_NAME) as db:
        db.execute(
            """
            CREATE TABLE IF NOT EXISTS search_logs (
                city TEXT,
                temperature REAL,
                humidity REAL,
                wind_speed REAL,
                searched_at TEXT
            )
            """
        )
        db.write_single_record(
            "search_logs",
            {
                "city": city,
                "temperature": temperature,
                "humidity": humidity,
                "wind_speed": wind_speed,
                "searched_at": datetime.now().isoformat(timespec="seconds"),
            },
        )


def read_logs():
    """Visszaadja az eddigi kereséseket DataFrame-ként."""
    try:
        with SQLiteDB(DB_NAME) as db:
            return pd.read_sql_query(
                "SELECT * FROM search_logs ORDER BY searched_at DESC", db.connection
            )
    except (sqlite3.Error, pd.errors.DatabaseError):
        return pd.DataFrame()


def main():
    st.set_page_config(page_title="Weather Dashboard", page_icon="🌤️", layout="wide")
    st.title("🌤️ Robot Dreams Python – Weather Map & Data Visualization App")

    with st.sidebar:
        st.header("⚙️ Keresés")
        with st.form("city_form"):
            city_input = st.text_input(
                "Add meg egy város nevét",
                value="Budapest",
                placeholder="pl. Diósd, Szeged, London",
            )
            submitted = st.form_submit_button("Lekérdezés")

    location = get_coordinates(city_input)
    if location is None:
        st.warning(
            f"Nem található '{city_input}' nevű város, vagy hiba történt a "
            "geocoding API hívásakor. Próbálj meg egy másik nevet."
        )
        st.stop()

    weather = get_weather(location["lat"], location["lon"])
    if weather is None or "current" not in weather:
        st.warning("Nem sikerült lekérni az időjárási adatokat. Próbáld újra később.")
        st.stop()

    current = weather["current"]
    temperature = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    wind_speed = current["wind_speed_10m"]

    st.subheader(f"Jelenlegi időjárás itt: {location['name']}, {location['country']}")

    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Hőmérséklet (°C)", f"{temperature} °C")
    kpi2.metric("Páratartalom (%)", f"{humidity} %")
    kpi3.metric("Szélsebesség (km/h)", f"{wind_speed} km/h")

    st.divider()

    tab_map, tab_forecast, tab_history = st.tabs(
        ["🗺️ Térkép", "📈 Előrejelzés", "🗂️ Keresési előzmények"]
    )

    with tab_map:
        st.subheader(f"Térkép – {location['name']}")
        map_df = pd.DataFrame([{"lat": location["lat"], "lon": location["lon"]}])
        st.map(map_df, zoom=10)

    with tab_forecast:
        st.subheader("Óránkénti hőmérséklet-előrejelzés (következő 5 nap)")
        hourly = weather["hourly"]
        forecast_df = pd.DataFrame(
            {
                "Idő": pd.to_datetime(hourly["time"]),
                "Hőmérséklet (°C)": hourly["temperature_2m"],
            }
        )
        fig = px.line(
            forecast_df,
            x="Idő",
            y="Hőmérséklet (°C)",
            title=f"{location['name']} – óránkénti hőmérséklet",
        )
        st.plotly_chart(fig, width="stretch")

    log_search(location["name"], temperature, humidity, wind_speed)

    with tab_history:
        st.subheader("Eddigi keresések (sqlite adatbázisból)")
        logs_df = read_logs()
        if logs_df.empty:
            st.info("Még nincs elmentett keresés.")
        else:
            st.dataframe(logs_df, width="stretch")


if __name__ == "__main__":
    main()