from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#Part 1
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
    new_movie = {'id' : , "" : movie.title, "" : movie.director, "year" : movie.year}
    movies.append(new_movie)
    return new_movie