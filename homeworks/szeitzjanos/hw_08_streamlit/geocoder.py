import requests

class GeoCoder:
    ''' Returns coordinates from the Open-Meteo geocoding API based on a city name. '''

    BASE_URL = 'https://geocoding-api.open-meteo.com/v1/search'

    def get_coordinates(self, city_name: str):
        params = {'name': city_name, 'count': 1, 'language': 'en', 'format': 'json'}
        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            raise ValueError('Geocoding API error!')

        data = response.json()

        if 'results' not in data or len(data['results']) == 0:
            raise ValueError('City not found!')

        result = data['results'][0]
        return {
            'city': result['name'],
            'country': result['country'],
            'lat': result['latitude'],
            'lon': result['longitude']
        }
