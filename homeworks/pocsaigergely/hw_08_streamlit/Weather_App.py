import requests
import pandas as pd
import plotly.express as px
import streamlit as st


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
OPENMET_URL = "https://api.open-meteo.com/v1/forecast"


#GET CITY COORDINATES DATA
@st.cache_data(ttl=1000)
def get_coordinates(city_name):

    params = {"name": city_name, "count": 1, "language": "hu", "format": "json"}
    response = requests.get(GEOCODING_URL, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    if "results" not in data:
        return None
    data_dict = data["results"][0]

 #   st.caption(data_dict)


    return {
        "name": data_dict["name"],
        "country": data_dict.get("country", "Ismeretlen"),
        "lat": data_dict["latitude"],
        "lon": data_dict["longitude"],
            }


#FROM CITY COORDINATES GET WEATHER DATA
@st.cache_data(ttl=1000)
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
    response = requests.get(OPENMET_URL, params=params)
    if response.status_code != 200:
        return None
    return response.json()
    
    
def process_data(data):

    if "hourly" in data:
        df = pd.DataFrame(data["hourly"])
        df["time"] = pd.to_datetime(df["time"])
        df.set_index("time", inplace=True)
 #       df = df.rename(columns={"o": "Open", "h": "High", "l": "Low", "c": "Close", "v": "Volume"})
 #       df = df.drop(columns={"t", "vw", "n"})
 #       df = df.sort_index()
 #       numeric_columns = ["Open", "High", "Low", "Close", "Volume"]
 #       df[numeric_columns] = df[numeric_columns].astype(float)
        print(df)
        return df
    
 #       df2 = pd.DataFrame(data["current"])
        

    else:
        st.error("No data available")
        return None
    




def main():

    st.title("Robot Dreams Python - Weather Map & Data Visualization App")
    st.subheader("(Gergely Pocsai)")


    city_input = st.text_input("Name of city",
    value="Budapest",
    placeholder="Type here a valid city name",
            )


    location = get_coordinates(city_input)
    if location is None:
        st.warning(
            f"Cant find '{city_input}' city"
        )
        st.stop()

    st.caption(location)

    weather_data = get_weather(location["lat"], location["lon"])
    if weather_data is None or "current" not in weather_data:
        st.warning("Nem sikerült lekérni az időjárási adatokat. Próbáld újra később.")
        st.stop()



    st.subheader(f"Jelenlegi időjárás itt: {location['name']}, {location['country']}")
    st.caption(weather_data)


    if weather_data:
        df = process_data(weather_data)

    st.dataframe(df)

#LINE CHART

    if df is not None:

        st.subheader("Hourly forecast")
        fig_close = px.line(
            df,
            x = df.index,
            y="temperature_2m",
            title=f"{city_input} Temperature at 2m height"

        )
        st.plotly_chart(fig_close)

    else:
        st.error("No data available. Check the symbol!")

if __name__ == "__main__":
    main()