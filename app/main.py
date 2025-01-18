from fastapi import FastAPI
from database.type import MovieOut, MovieIn
from typing import List
from database.session import Session, engine
from database import models

app = FastAPI()
db = Session()

@app.get("/filmes", response_model=List[MovieOut])
async def get_all_movies():
    movies = db.query(models.Movie).all()
    return movies

@app.get("/filmes/{id}", response_model=MovieOut)
async def get_movie(id: int):
    movie = db.query(models.Movie).filter(models.Movie.id == id).first()
    return movie

@app.post("/filmes", response_model=MovieOut)
async def create_movie(movie: MovieIn):
    new_movie = models.Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie