#api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxx"

import requests

api = "https://api.openweathermap.org/data/2.5/weather?lat=52.250594&lon=21.172994&appid=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


response = requests.get(url=api)
print(response)
data_json = response.json()
print(data_json)
weather_id = response.json()["weather"][0]["id"]
print(weather_id) #803
weather_sky_01 = response.json()["weather"][0]["main"]
weather_sky_01 = response.json()["weather"][0]["description"]

temp = response.json()['main']['temp']
print(temp) # 288.35
pressure = response.json()["main"]['pressure']
print(pressure) #1025

print("================================= OPCJA NR2 ===================================================================================================")

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
parameters = {
    "lat":52.250594,
    "lon":21.17299,
    "appid":api_key


}

response = requests.get(url=OWM_endpoint, params=parameters)
print(response.json())










