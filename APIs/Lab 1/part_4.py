import json, os, time
import api_client as ac

#json.dump(data, file)
#json.load(file)
#os.path.exists(path)
#os.path.getmtime(path)
#time.time()

#Took the functions from part_2.py directly.
def find_city(name : str) -> dict: 
    response = ac.get_json("https://geocoding-api.open-meteo.com/v1/search", params={"name" : name, "count" : 1})
    if response.get("results") == None:
          print("Could not find this city.")
          return
    
    return response

def get_weather(latitude : float, longitude : float) -> dict: 
        response = ac.get_json("https://api.open-meteo.com/v1/forecast", params={"latitude" : latitude, "longitude" : longitude, "current": ["temperature_2m", "wind_speed_10m"]})
        return response


# #Comparison on time. This needs to be seamed together/integrated with the upper part.
path = "./weather.json"

if os.path.exists(path) and (time.time() - os.path.getmtime(path)) <= (10 * 60):
    print("File existed and is not 10 minutes old yet.")
    weather = json.load(path)
else:
    print("...")
    city = input("Name a city> ").strip()
    found_city = find_city(city)
    weather = get_weather(found_city["results"][0]["latitude"], found_city["results"][0]["longitude"])

    json.dump(weather, path)
    