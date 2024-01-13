from fastapi import FastAPI
import numpy as np
from typing import List


# from com import compute_dot_product
from models import RequestBody, ResponseBody


app = FastAPI()

@app.get("/")
def index():
    return {"greeting": "Hello world, everything is up and running!"}


# @app.post("/dot")