from api_client import get_json
import requests

BASE = "http://127.0.0.1:8000"

movies = get_json(f"{BASE}/movies")

non_existing_movie = get_json(f"{BASE}/movies/1000")
#Gives: "The server said no: 404"

movie = {"title" : "The Maltese Falcon", "director" : "John Huston", "year" : 1941}
response = requests.post(f"{BASE}/movies", json=movie, timeout=3)
print(response.status_code)
#Gives "201" (= create)