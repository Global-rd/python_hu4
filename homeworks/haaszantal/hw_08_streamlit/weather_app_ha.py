import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
import requests

st.markdown("""
    <style>
    /* Submit gomb */
    div.stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-weight: bold;
    }

    /* Hover effekt */
    div.stButton > button:hover {
        background-color: #45a049;
        transition: 0.3s;
    }

    /* Subheader (EZ a működő selector) */
    [data-testid="stSubheader"] {
        color: #4CAF50 !important;
        font-weight: 600;
    }

    /* Input mező alap állapot */
    div[data-testid="stTextInput"] input {
        border: 2px solid #a5d6a7;   /* halvány zöld */
        border-radius: 8px;
    }

    [data-testid="stAppViewContainer"] {
        max-width: 900px;
        margin: 40px auto;
        padding: 30px;
        border: 1.5px solid #81c784;
        border-radius: 12px;
        background-color: #f1f8f4;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }

    [data-testid="stAppViewContainer"] > div > div {
    background-color: #dcefe3 !important;
    }

    </style>
""", unsafe_allow_html=True)


GEO_BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"

#cím formázva
st.markdown(
    "<h1 style='color:#4CAF50;'>Robot Dreams Python - Weather Map & Data Visualization App</h1>",
    unsafe_allow_html=True
)

#st.subheader("Enter City name")
city = st.text_input("", value="Enter City name")

#az input értékét eltárolom egy változóban
submitted = st.button("Submit")

geo_url = f"{GEO_BASE_URL}?name={city}"

if submitted:
    response_geo = requests.get(geo_url)

    if response_geo.status_code == 200:
        geo_data = response_geo.json()

        if "results" in geo_data:

            if geo_data["results"]: 
               data_latitude = geo_data["results"][0]["latitude"] 
               data_longitude = geo_data["results"][0]["longitude"]
               country = geo_data["results"][0]["country"]

               FRC_BASE_URL = "https://api.open-meteo.com/v1/forecast"

               params = {"latitude": data_latitude,
                         "longitude": data_longitude,
                         "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
                         "hourly": "temperature_2m"}

               response_frc = requests.get(FRC_BASE_URL, params=params)

               if response_frc.status_code == 200:
                  frc_data = response_frc.json()
                  
                  current = frc_data["current"]

                  temperature = current["temperature_2m"]
                  humidity = current["relative_humidity_2m"]
                  wind = current["wind_speed_10m"]

                  st.divider()

                  #Formázott subheader
                  st.markdown(
                      f"<h3 style='color:#ff9800'>Current Weather in {city}, {country}</h3>",
                      unsafe_allow_html=True
                  )

                  kpi1, kpi2, kpi3 = st.columns(3)

                  #KPI
                  with kpi1:
                       st.metric(
                          label="Current temperature", value=f"{temperature} °C"
                                 )
                  with kpi2:
                       st.metric(
                          label="Relative humidity", value=f"{humidity} %"

                                 )
                  with kpi3:
                       st.metric(
                          label="Wind speed", value=f"{wind} km/h"
                       )
                  
                  df_map = pd.DataFrame({
                    "lat": [data_latitude],
                    "lon": [data_longitude]
                  })

                  st.divider()

                  #subheader formázva
                  st.markdown(
                        "<h3 style='color:#ff9800'>🗺️ Weather Map</h3>",
                        unsafe_allow_html=True
                  )

                  st.map(df_map)
                  
                  #LINE CHART
                  hourly= frc_data["hourly"]
                  df = pd.DataFrame(hourly)
                  df["time"] = pd.to_datetime(df["time"])

                  st.divider()

                  #Formázott subheader
                  st.markdown(
                      "<h3 style='color:#ff9800'>📈 Hourly Temperature Forecast (Next 5 Day</h3>",
                      unsafe_allow_html=True
                  )

                  fig = px.line(
                     df,
                     x="time",
                     y="temperature_2m"
                  )

                  fig.update_xaxes(
                      dtick=21600000,
                      tickformat="%H:%M\n%b %d"
                  )

                  fig.update_layout(
                      xaxis_title="Time",
                      yaxis_title="Temperature (°C)",
                      xaxis=dict(
                        tickformat="%H:%M\n%b %d"
                      )
                  )

                  st.plotly_chart(fig)

               else:
                  st.error(f"Failed to fetch data: {response_frc.status_code} - {response_frc.text}")

            else:    
               st.warning("Nincs találat!")
        else:
            st.warning("Hibás városnév")

    else:
        st.error(f"Failed to fetch data: {response_geo.status_code} - {response_geo.text}")
    

    #az app webcíme: https://haaszantalweatherapp.streamlit.app/
    
    

        

    
