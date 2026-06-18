
import requests
import pandas as pd
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Weather Dashboard",
      layout="wide",
)

st.title("Weather Dashboard")

with st.sidebar:
    st.header("City Selection")
    city_input = st.text_input("Enter a city name:", value="Budapest")
    submit = st.button("Search")

if not submit:
    st.stop()

if not city_input.strip():
    st.warning("Please enter a valid city name.")
    st.stop()

geocoding_url = "https://geocoding-api.open-meteo.com/v1/search"
geocoding_params = {
    "name": city_input,
    "count": 1,
    "language": "en",
    "format": "json",
}

try:
    geo_resp = requests.get(geocoding_url, params=geocoding_params, timeout=10)
    geo_resp.raise_for_status()
    geo_data = geo_resp.json()
except Exception:
    st.warning("Geocoding API error. Try again later or use another city.")
    st.stop()

results = geo_data.get("results")
if not results:
    st.warning("City not found. Check the spelling.")
    st.stop()

location = results[0]
lat = location["latitude"]
lon = location["longitude"]
city_name = location["name"]
country_name = location.get("country", "Unknown")

st.subheader(f"Current Weather in {city_name}, {country_name}")

forecast_url = "https://api.open-meteo.com/v1/forecast"
forecast_params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True,
    "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m",
    "forecast_days": 5,
    "timezone": "auto",
}

try:
    forecast_resp = requests.get(forecast_url, params=forecast_params, timeout=10)
    forecast_resp.raise_for_status()
    forecast_data = forecast_resp.json()
except Exception:
    st.warning("Forecast API error. Try again later.")
    st.stop()

current = forecast_data.get("current_weather")
hourly = forecast_data.get("hourly")

if not current or not hourly:
    st.warning("Weather data unavailable.")
    st.stop()

current_temp = current.get("temperature")
current_wind = current.get("windspeed")
current_time_str = current.get("time")

hourly_times = hourly.get("time", [])
hourly_humidity = hourly.get("relativehumidity_2m", [])

humidity_value = None
if current_time_str in hourly_times:
    idx = hourly_times.index(current_time_str)
    if 0 <= idx < len(hourly_humidity):
        humidity_value = hourly_humidity[idx]
if humidity_value is None and hourly_humidity:
    humidity_value = hourly_humidity[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Temperature (°C)",
        value=f"{current_temp:.1f}" if current_temp is not None else "N/A",
    )

with col2:
    st.metric(
        label="Humidity (%)",
        value=f"{humidity_value:.0f}" if humidity_value is not None else "N/A",
    )

with col3:
    st.metric(
        label="Wind Speed (km/h)",
        value=f"{current_wind:.1f}" if current_wind is not None else "N/A",
    )

st.markdown("---")

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Hourly Temperature Forecast (Next 5 Days)")

    hourly_temp = hourly.get("temperature_2m", [])
    if hourly_times and hourly_temp:
        df = pd.DataFrame(
            {
                "time": pd.to_datetime(hourly_times),
                "temperature_2m": hourly_temp,
            }
        )
        df = df.set_index("time")
        st.line_chart(df["temperature_2m"])
    else:
        st.info("No forecast data available for the chart.")

with right_col:
    st.subheader("Map View")
    map_df = pd.DataFrame(
        {
            "lat": [lat],
            "lon": [lon],
        }
    )
    st.map(map_df, zoom=9)

st.caption(
    f"Data source: Open-Meteo API | City: {city_name}, {country_name} | Coordinates: {lat:.3f}, {lon:.3f}"
)

city_name = location["name"]
country_name = location.get("country", "Ismeretlen ország")

st.subheader(f"Current Weather: {city_name}, {country_name}")

forecast_url = "https://api.open-meteo.com/v1/forecast"
forecast_params = {
    "latitude": lat,
    "longitude": lon,
    "current_weather": True,
    "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m",
    "forecast_days": 5,
    "timezone": "auto",
}

try:
    forecast_resp = requests.get(forecast_url, params=forecast_params, timeout=10)
    forecast_resp.raise_for_status()
    forecast_data = forecast_resp.json()
except Exception:
    st.warning("Hiba történt a forecast API hívása közben. Próbáld meg később.")
    st.stop()

current = forecast_data.get("current_weather")
hourly = forecast_data.get("hourly")

if not current or not hourly:
    st.warning("Nem sikerült lekérni az időjárási adatokat.")
    st.stop()

current_temp = current.get("temperature")
current_wind = current.get("windspeed")
current_time_str = current.get("time")

hourly_times = hourly.get("time", [])
hourly_humidity = hourly.get("relativehumidity_2m", [])

humidity_value = None
if current_time_str in hourly_times:
    idx = hourly_times.index(current_time_str)
    if 0 <= idx < len(hourly_humidity):
        humidity_value = hourly_humidity[idx]
if humidity_value is None and hourly_humidity:
    humidity_value = hourly_humidity[0]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Temperature (°C)",
        value=f"{current_temp:.1f}" if current_temp is not None else "N/A",
    )

with col2:
    st.metric(
        label="Humidity (%)",
        value=f"{humidity_value:.0f}" if humidity_value is not None else "N/A",
    )

with col3:
    st.metric(
        label="Wing Speed (km/h)",
        value=f"{current_wind:.1f}" if current_wind is not None else "N/A",
    )

st.markdown("---")

left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("Hourly Temperature Forecast (Next 5 Days)")

    hourly_temp = hourly.get("temperature_2m", [])
    if hourly_times and hourly_temp:
        df = pd.DataFrame(
            {
                "time": pd.to_datetime(hourly_times),
                "temperature_2m": hourly_temp,
            }
        )
        df = df.set_index("time")
        st.line_chart(df["temperature_2m"])
    else:
        st.info("Nem áll rendelkezésre előrejelzési adat a grafikonhoz.")

with right_col:
    st.subheader("Térképes megjelenítés")
    map_df = pd.DataFrame(
        {
            "lat": [lat],
            "lon": [lon],
        }
    )
    st.map(map_df, zoom=9)

st.caption(
    f"Adatok forrása: Open-Meteo API | Város: {city_name}, {country_name} | Koordináták: {lat:.3f}, {lon:.3f}"
)
