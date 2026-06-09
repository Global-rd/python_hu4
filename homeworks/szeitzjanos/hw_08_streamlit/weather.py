import requests

class WeatherClient:
    ''' Retrieves weather data from the Open-Meteo forecast API. '''

    BASE_URL = 'https://api.open-meteo.com/v1/forecast'

    def get_weather(self, lat: float, lon: float):
        params = {
            'latitude': lat,
            'longitude': lon,
            'current_weather': True,
            'hourly': 'temperature_2m,relative_humidity_2m',
            'forecast_days': 5,
            'timezone': 'auto'
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            raise ValueError('Weather API error!')

        data = response.json()

        current = data['current_weather']

        return {
            'temperature': current['temperature'],
            'windspeed': current['windspeed'],
            'humidity': data.get('hourly', {}).get('relative_humidity_2m', [None])[0],
            'hourly_time': data['hourly']['time'],
            'hourly_temp': data['hourly']['temperature_2m']
        }

'''
'humidity': data.get('hourly', {}).get('relativehumidity_2m', [None])[0],
'''