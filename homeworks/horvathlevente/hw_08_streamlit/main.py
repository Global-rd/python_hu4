import streamlit as st
import requests
import pandas as pd
import sqlite3
from datetime import datetime

st.set_page_config(page_title="Weather Dashboard", layout="wide")

# -----------------------------
# SQLite adatbázis inicializálás
# -----------------------------
def init_db():
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            city TEXT,
            temperature REAL,
            humidity REAL,
            windspeed REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_search(city, temp, hum, wind):
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs VALUES (?, ?, ?, ?, ?)",
        (city, temp, hum, wind, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )
    conn.commit()
    conn.close()

init_db()

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌦️ Weather Forecast Dashboard")

city = st.text_input("Enter city name", "Diósd")

if city:
    # -----------------------------
    # 1. Geocoding API
    # -----------------------------
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {"name": city, "count": 1, "language": "en", "format": "json"}

    geo_response = requests.get(geo_url, params=geo_params)

    if geo_response.status_code != 200 or "results" not in geo_response.json():
        st.warning("⚠️ City not found or API error.")
    else:
        result = geo_response.json()["results"][0]
        lat = result["latitude"]
        lon = result["longitude"]
        country = result["country"]

        st.subheader(f"Current Weather in {city}, {country}")

        # -----------------------------
        # 2. Forecast API
        # -----------------------------
        forecast_url = "https://api.open-meteo.com/v1/forecast"
        forecast_params = {
            "latitude": lat,
            "longitude": lon,
            "current_weather": True,
            "hourly": "temperature_2m",
            "timezone": "auto"
        }

        forecast_response = requests.get(forecast_url, params=forecast_params)

        if forecast_response.status_code != 200:
            st.warning("⚠️ Forecast API error.")
        else:
            data = forecast_response.json()

            # Current weather
            temp = data["current_weather"]["temperature"]
            wind = data["current_weather"]["windspeed"]
            humidity = data.get("hourly", {}).get("relativehumidity_2m", [None])[0]

            # KPI-ok
            col1, col2, col3 = st.columns(3)
            col1.metric("🌡 Temperature (°C)", f"{temp}°C")
            col2.metric("💧 Humidity (%)", f"{humidity}%")
            col3.metric("💨 Wind Speed (km/h)", f"{wind} km/h")

            # Logolás
            log_search(city, temp, humidity, wind)

            # -----------------------------
            # 3. Hourly forecast chart
            # -----------------------------
            hourly_df = pd.DataFrame({
                "time": data["hourly"]["time"],
                "temperature": data["hourly"]["temperature_2m"]
            })

            hourly_df["time"] = pd.to_datetime(hourly_df["time"])

            st.subheader("📈 Hourly Temperature Forecast (Next 5 Days)")
            st.line_chart(hourly_df, x="time", y="temperature")
            # -----------------------------
            # 4. Map megjelenítése
            # -----------------------------
            st.subheader("🗺️ Weather Map")

            map_df = pd.DataFrame({
                "lat": [lat],
                "lon": [lon]
            })

            st.map(map_df, zoom=10)

