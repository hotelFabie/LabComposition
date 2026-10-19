import os 
from dotenv import load_dotenv
import requests
import api_client as ac

#1
#Done

#2
#Done

#3 
#The exact directory is hidden, for privacy reasons. 
load_dotenv("../Resources/API/.env")
token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization" : f"Bearer {token}"}

username = input("Username: ").strip()

response = ac.get_json(f"https://api.github.com/users/{username}/repos", params={"sort": "pushed", "per_page" : 5}, headers=headers)

#4
response_has_token = requests.get(f"https://api.github.com/users/{username}/repos")
print(response_has_token.headers["X-RateLimit-Limit"])
#60

#Comparison
response_no_token = requests.get(f"https://api.github.com/users/{username}/repos", params={"sort": "pushed", "per_page" : 5}, headers=headers)
print(response_no_token.headers["X-RateLimit-Limit"])
#5000

#5
broken_response = requests.get(f"https://api.github.com/users/{username}/repos", params={"sort": "pushed", "per_page" : 5}, headers=headers)
print(broken_response.status_code)
print(broken_response.json())
#Got 401
#401 = You're not known to the page, and therefore not trusted. [Unauthorized]
#403 = You're known to page, and also denied entry. [Forbidden]

#6
#.env did not show up.

#7
#Token deleted. :)