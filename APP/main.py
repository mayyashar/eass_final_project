from fastapi import Depends, FastAPI
import numpy as np
from typing import List, Union
from pydantic import BaseModel
import psycopg2
# from sqlalchemy import create_engine, Column, Integer, String, Sequence
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# from com import compute_dot_product
DATABASE_URL = "postgresql://postgres:root@y172.17.0.2:5432/postgres"
        # user = 'postgres', password='root', host='172.17.0.2', port='5432')

def get_connection():
    connection = psycopg2.connect(DATABASE_URL)
    try:
        yield connection
    finally:
        connection.close()

print("May - postgres connected")

# from models import RequestBody, ResponseBody

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def index():
    return {"greeting": "Hello, everything is up and running!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}



    





# @app.post("/dot")