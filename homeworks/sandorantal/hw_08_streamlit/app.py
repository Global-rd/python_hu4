import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import pydeck as pdk
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("weather_log.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            humidity REAL,
            wind_speed REAL,
            timestamp TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_to_db(city, temp, humidity, wind):
    conn = sqlite3.connect("weather_log.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temp, humidity, wind, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

init_db()

st.set_page_config(page_title="Robot Dreams Weather App", layout="wide")

st.title("Robot Dreams Python - Weather Map & Data Visualization App")

city_input = st.text_input("Enter city name", value="Diósd")

if city_input:
    geocoding_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_input}&count=1&language=en&format=json"
    
    try:
        geo_response = requests.get(geocoding_url).json()
        
        if "results" not in geo_response or len(geo_response["results"]) == 0:
            st.warning(f"Not found '{city_input}' city ​​named. Please check your typing!")
        else:
            geo_data = geo_response["results"][0]
            lat = geo_data["latitude"]
            lon = geo_data["longitude"]
            city_name = geo_data["name"]
            country = geo_data.get("country", "")
            
            forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relative_humidity_2m&wind_speed_unit=kmh"
            forecast_response = requests.get(forecast_url).json()
            
            current_weather = forecast_response["current_weather"]
            
            temp = current_weather["temperature"]
            wind_speed = current_weather["windspeed"]
            
            humidity = forecast_response["hourly"]["relative_humidity_2m"][0]
            
            log_to_db(city_name, temp, humidity, wind_speed)
            
            st.header(f"Current Weather in {city_name}, {country}")
            
            col1, col2, col3 = st.columns(3)
            col1.metric(label="Temperature (°C)", value=f"{temp}°C")
            col2.metric(label="Humidity (%)", value=f"{humidity}%")
            col3.metric(label="Wind Speed (km/h)", value=f"{wind_speed} km/h")
            
            st.subheader("Weather Map")
            
            map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})
            
            st.pydeck_chart(pdk.Deck(
                map_style='mapbox://styles/mapbox/dark-v10',
                initial_view_state=pdk.ViewState(
                    latitude=lat,
                    longitude=lon,
                    zoom=11,
                    pitch=0,
                ),
                layers=[
                    pdk.Layer(
                        'ScatterplotLayer',
                        data=map_data,
                        get_position='[lon, lat]',
                        get_color='[200, 30, 30, 160]',
                        get_radius=200,
                    ),
                ],
            ))
            
            st.subheader("Hourly Temperature Forecast (Next 5 Days)")
            
            hourly_data = forecast_response["hourly"]
            df_hourly = pd.DataFrame({
                "Date": pd.to_datetime(hourly_data["time"]),
                "Temperature (°C)": hourly_data["temperature_2m"]
            })
            
            df_hourly["Display"] = df_hourly["Date"].dt.strftime("%m.%d %H:%M")
            
            fig = px.line(
                df_hourly, 
                x="Display", 
                y="Temperature (°C)",
                template="plotly_dark"
            )
            
            fig.update_layout(xaxis_tickangle=-90)
            st.plotly_chart(fig, use_container_width=True)
            
    except Exception as e:
        st.error(f"An error occurred while retrieving data.: {e}")