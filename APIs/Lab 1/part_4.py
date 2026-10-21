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
#1 and 2 both at once.

path : str = "./weather.json"

#os.path.getmtime() also considers time of most recent update, not just creation time.
if os.path.exists(path) and (time.time() - os.path.getmtime(path)) <= (10 * 60):
    print("File exists and is not 10 minutes old yet.")
    
    #Read
    with open(path, "r") as f:
        weather : dict = json.load(f)
        print(f"Read data from {path}.")
else:
    print("Attempt at writing.")
    city : str = "Copenhagen"
    found_city : str = find_city(city)
    weather : dict = get_weather(found_city["results"][0]["latitude"], found_city["results"][0]["longitude"])

    #Write    
    with open(path, "w") as f:
        json.dump(weather, f, indent = 2)
        print(f"Write to {path} done.")

#3
#Of course absolutely current real-time data should ideally represent the most accurate data.
#But in cases like with weather, where a time-frame of 10 minutes most likely won't see the weather shift with a drastic difference,
#storing fairly accurate data for a short period reduces data usage and both: [requests from the client + responses from the server].
#Furthermore, if the server is prone to easily punish multiple requests, you avoid the risk of demanding too much from the server.

#In short, you reduce redundant requests.