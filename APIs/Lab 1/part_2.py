import api_client as ac
import requests

#1
response_1 = ac.get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name" : "Stockholm", "count" : 1})

print(response_1)

latitude = response_1['results'][0]['latitude']
longitude = response_1['results'][0]['longitude']
print(f"Latitude: {latitude}, Longitude: {longitude}")

#2
response_2 = ac.get_json("https://api.open-meteo.com/v1/forecast", params={"latitude" : latitude, "longitude" : longitude, "current": ["temperature_2m", "wind_speed_10m"]})
print(response_2)

#3
def find_city(name : str) -> dict: 
    response = ac.get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name" : city, "count" : 1})
    return response

def get_weather(latitude : float, longitude : float) -> dict: 
    response = ac.get_json("https://api.open-meteo.com/v1/forecast", params={"latitude" : latitude, "longitude" : longitude, "current": ["temperature_2m", "wind_speed_10m"]})
    return response

#_____

city = input("City> ")

found_city = find_city(city)

weather = get_weather(found_city['results'][0]['latitude'], found_city['results'][0]['longitude'])

#Presentable format
print(f"{found_city['results'][0]['name']}, {found_city['results'][0]['country']}: {weather["current"]["temperature_2m"]}°C, wind: {weather["current"]["wind_speed_10m"]} km/h.")

#4
