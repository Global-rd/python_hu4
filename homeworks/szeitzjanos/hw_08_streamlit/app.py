import streamlit as st
import pandas as pd

from geocoder import GeoCoder
from weather import WeatherClient
from logger import SearchLogger


def main():

    st.set_page_config(page_title='Weather Dashboard', layout='wide')

    geocoder = GeoCoder()
    weather_client = WeatherClient()
    logger = SearchLogger()

    st.title('🌦️ sei.lethargy python - weather dashboard 🌦️')
    st.title('map data visualisation application')

    city_input = st.text_input('Enter city name', 'Győr')

    if st.button('Search'):
        try:
            location = geocoder.get_coordinates(city_input)
            st.subheader(f"Current Weather in {location['city']}, {location['country']}")
            weather = weather_client.get_weather(location['lat'], location['lon'])
            col1, col2, col3 = st.columns(3)
            col1.metric('Temperature (°C)', f"{weather['temperature']}°C")
            col2.metric('Humidity (%)', f"{weather['humidity']}%")
            col3.metric('Wind Speed (km/h)', f"{weather['windspeed']} km/h")
            logger.log(
                city=location['city'],
                temperature=weather['temperature'],
                humidity=weather['humidity'],
                windspeed=weather['windspeed']
            )

            map_df = pd.DataFrame({
                "lat": [location["lat"]],
                "lon": [location["lon"]]
            })
            st.subheader('Weather Map')
            st.map(map_df, zoom=12)

            df = pd.DataFrame({
                'time': pd.to_datetime(weather['hourly_time']),
                'temperature': weather['hourly_temp']
            })
            st.subheader('Hourly Temperature Forecast (Next 5 Days)')
            df['timestr'] = df['time'].dt.strftime('%m.%d %H:%M')
            st.line_chart(df, x='timestr', x_label='', y='temperature', y_label='')

        except Exception as e:
            st.warning(f'Error: {e}')

if __name__ == "__main__":
    main()