import json, os, time
import api_client as ac

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

#_____

path = "./weather.json"

#There may be something not fully correct with how I have structured the conditions here.
if os.path.exists(path) and (time.time() - os.path.getmtime(path)) <= (10 * 60):
    print("File existed and is not 10 minutes old yet.")
    
    #This needs some sort of loading...
    with open(path, "r") as f:
        weather : dict = json.load(path)
else:
    print("...")
    city : str = "Copenhagen"
    found_city : str = find_city(city)
    weather : dict = get_weather(found_city["results"][0]["latitude"], found_city["results"][0]["longitude"])

    with open(path, "w") as f:
        json.dump(weather, f)