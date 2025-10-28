from fastapi import FastAPI, HTTPException
from typing import List
import uvicorn
import database
import models
from models import Movie, MovieCreate


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}


 
 
@app.post("/movies/" , response_model=Movie)
def create_movie(movie:MovieCreate):
    """ Creates a new movie in the database """
    movie_id = database.create_movie(movie)
    return models.Movie(id=movie_id , **movie.dict())


@app.get("/movies/{movie_id}" , response_model=Movie)
def read_movie(movie_id: int):
    """ reads out movies from database single movies"""
    movie = database.read_movie(movie_id)
    if movie is None:
       raise HTTPException(status_code=404 , detail="MOVIE NOT FOUND ")
    return movie
@app.put("/movies/{movie_id}" , response_model=Movie)
def update_movie(movie_id: int , movie:MovieCreate):
    """ Updates the movies"""
    updated = database.update_movie(movie_id , movie)
    if not updated:
        raise HTTPException(status_code=404 , detail="Movie not found")
    return models.Movie(id=movie_id , **movie.dict())



@app.delete("/movies/{movie_id}" , response_model=dict)
def delete_movie(movie_id:int):
    """deletes a movie"""
    deleted = database.delete_movie(movie_id)
    if not deleted:
        raise HTTPException(status_code=404 , detail="Movie not found")
    return {"message": "Movie deleted successfully"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)