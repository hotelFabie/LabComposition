#This is essentially Part 1. The lab expected this naming.

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

@app.post("/movies", status_code=201)
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

@app.put("/movies/{movie_id}")
def replace_movie(movie_id : int, movie : Movie):
    current_movie = find_movie(movie_id)
    current_movie['title'] = movie.title
    current_movie['director'] = movie.director
    current_movie['year'] = movie.year
    return current_movie

@app.delete("/movies/{movie_id}", status_code=204)
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
@app.patch("/movies/{movie_id}")
def patch_movie(movie_id : int, movie : MovieUpdate):
    current_movie = find_movie(movie_id)
    changes = movie.model_dump(exclude_unset=True)
    current_movie.update(changes)

    return current_movie

#2
#Only the year was changed.

#3
#"Test the edges"