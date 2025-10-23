from fastapi import FastAPI
from typing import List
import database
from models import Movie, MovieCreate
import models

app= FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcometo crud"}