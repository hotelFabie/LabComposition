#This is essentially Part 1. The lab expected this naming.

from fastapi import FastAPI, HTTPException, Header, Depends
from pydantic import BaseModel

import os
from dotenv import load_dotenv

import json

#____________________
#Part 3 - #2
load_dotenv("D:/Programming/Lexicon/Resources/API2/.env")
API_KEY = os.getenv("API_KEY")

def check_key(x_api_key: str | None = Header(default=None)):
    print(API_KEY)
    if API_KEY is None or x_api_key != API_KEY:
        raise HTTPException(status_code=401)
#Part 4 - Applying this function to all the CRUD methods/functions we implement (besides GET).
#____________________

#1
app = FastAPI()
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
#3
@app.get("/movies")
def get_movies(director : str | None = None, year: int | None = None): 
    #Cover all bases.
    if director and year:
        return [movie for movie in movies 
                if director.lower() in movies["director"].lower()
                and year in movies["year"]]
    elif director:
        return [movie for movie in movies 
            if director.lower() in movies["director"].lower()]
    elif year:
        return [movie for movie in movies 
            if year == movie["year"]]
    return movies

#2
@app.get("/movies/{movie_id}")
def get_movie(movie_id : int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code = 404, detail="The movie was not found.")

#4
class Movie(BaseModel):
    title : str
    director : str
    year : int

#, status_code=201
@app.post("/movies", dependencies=[Depends(check_key)])
def create_movie(movie : Movie):
    latest_id = max([movie["id"] for movie in movies], default=0) + 1
    new_movie = {'id' : latest_id, "" : movie.title, "" : movie.director, "year" : movie.year}
    movies.append(new_movie)
    return new_movie

#4
#There will be two errors. First: missing director field - "type": "missing" - and Second: string cannot be parsed to integer - "type": "int_parsing"

#5
def find_movie(movie_id : int):
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    raise HTTPException(status_code=404, detail="The movie was not found.")

@app.put("/movies/{movie_id}", dependencies=[Depends(check_key)])
def replace_movie(movie_id : int, movie : Movie):
    current_movie = find_movie(movie_id)
    current_movie['title'] = movie.title
    current_movie['director'] = movie.director
    current_movie['year'] = movie.year
    return current_movie

@app.delete("/movies/{movie_id}", dependencies=[Depends(check_key)], status_code=204)
def remove_book(movie_id : int):
    movie = find_movie(movie_id)
    movies.remove(movie)

#Deleting the same movie - by the same id - two times leads to a detail message saying "The movie was not found."

#6
#Done in client.py

#Part 2 
#1
class MovieUpdate(BaseModel):
    title: str | None = None
    director: str | None = None
    year: int | None = None

#Like PUT, but with the exclude_unset setting.
@app.patch("/movies/{movie_id}", dependencies=[Depends(check_key)])
def patch_movie(movie_id : int, movie : MovieUpdate):
    current_movie = find_movie(movie_id)
    changes = movie.model_dump(exclude_unset=True)
    current_movie.update(changes)

    return current_movie

#2
#Only the year was changed.

#3
#Empty body: 200 (Nothing is changed)
#Year written as text: 422 (It cannot take text for something meant as integer)
#id that does not exist: 404 (The movie was not found)

#4
#PATCH: As the name suggests, you patch up (in other words, alter/change) something about an existing thing.
#PUT: Replace everything in it; there is nothing to be patched. You alter the state completely. 

#Part 3
#1
#Stored the tokens in an external directory, as it does not need to be seen.

#2
#Added at the top of this file.

#3
#If API_KEY is missing in .env, it will be equal to None.
#So, the check will look like None != None, which is False, and therefore this will be bypassed
#unless we add a check for this. 

#4
#Added to all methods besides GET.

#5
#401 without a key. 201 with a key. 401 with an incorrect key.

#6
#Done in client.py

#7
#Only .gitignore is shown, and not .env.

#Part 4
path : str = "./movies.json"

#1
def load_movies():
    pass
    #Should be a GET request.
    #Since the Database will never really change, 

#1
def save_movies():
    #...
    with open(path, "w") as f:
        json.dump(..., f, indent = 2)
    

movies = load_movies()

#4
#*first part wip* 
#Databases are used for both data persistence, and depending on which database (type), concurrency.