from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
#fix this data soon.
movies = [
    {"id": 1, "title": "Princess Mononoke", "director": "Hayao Miyazaki", "year": 1997},
    {"id": 2, "title": "Howl's Moving Castle", "director": "Hayao Miyazaki", "year": 2004},
    {"id": 3, "title": "Ponyo", "director": "Hayao Miyazaki", "year": 2008},
    {"id": 4, "title": "Nausicaä of the Valley of the Wind", "director": "Hayao Miyazaki", "year": 1984}
]

@app.get("/")
def home():
    return {"message" : "Start page"}

#Basing the option to choose a director on the author parameter from the lecture.
@app.get("/movies")
def get_movies(director : str | None = None): 
    if director:
        return [movie for movie in movies if director.lower() in movies["director"].lower()]
    return movies