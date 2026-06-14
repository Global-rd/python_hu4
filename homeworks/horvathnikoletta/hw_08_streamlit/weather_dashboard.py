import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Robot Dreams Python- Weather Map&Data Visualization App",
    layout="wide"
)
st.title("Robot Dreams Python- Weather Map&Data Visualization App")

city = st.text_input("Enter city name",value="Biatorbágy")

@st.cache_data
def get_coordinates(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, verify=False)

    if response.status_code != 200:
        return None

    data = response.json()

    if "results" not in data:
        return None

    return data["results"][0]

@st.cache_data
def get_weather(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
    }

    response = requests.get(url, params=params, verify=False)

    if response.status_code != 200:
        return None

    return response.json()

if city:

    location = get_coordinates(city)

    if not location:
        st.warning("City not found or API error.")
        st.stop()

    lat = location["latitude"]
    lon = location["longitude"]
    city_name = location["name"]
    country = location["country"]

    weather = get_weather(lat, lon)

    if not weather:
        st.warning("Weather API error.")
        st.stop()

    current = weather["current"]

    st.header(f"Current Weather in {city_name}, {country}")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Temperature(°C)",
        f"{current['temperature_2m']} °C"
    )

    col2.metric(
        "Humidity(%)",
        f"{current['relative_humidity_2m']} %"
    )

    col3.metric(
        "Wind Speed(km/h)",
        f"{current['wind_speed_10m']} km/h"
    )

    st.divider()
    st.subheader("Weather Map")

    map_df = pd.DataFrame({
        "lat": [lat],
        "lon": [lon]
    })

    st.map(map_df)

