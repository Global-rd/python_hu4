import requests
import settings as s

URL = "https://api.openweathermap.org/data/2.5/weather"

params = {"lat": s.BUDAPEST["lat"],
          "lon": s.BUDAPEST["lon"],
          "appid": s.OPENWEATHERMAP_API_KEY,
          "units": "metric"}

response = requests.get(url=URL, params=params).json()

print(type(response))

city = response["name"]
print(city)
temp = response["main"]["temp"]
print(temp)
