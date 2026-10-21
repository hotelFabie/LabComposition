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

#Part 3 - #6
import os
from dotenv import load_dotenv

load_dotenv("D:/Programming/Lexicon/Resources/API2/.env")
key = os.getenv("API_KEY")

#With key
movie_key = {"title" : "Zootopia", "director" : "Rich Moore", "year" : 2016}
response_with_key = requests.post(f"{BASE}/movies", json=movie_key, timeout=5, headers={"X-API-Key": key})
print(response_with_key.status_code)
#Gives 201

#Without key
movie_no_key = {"title" : "Zootopia 2", "director" : "Jared Bush", "year" : 2025}
response_without_key = requests.post(f"{BASE}/movies", json=movie_no_key, timeout=5)
print(response_without_key.status_code)
#Gives 401