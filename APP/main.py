from fastapi import Depends, FastAPI, Request, HTTPException
import numpy as np
from typing import List, Union
from pydantic import BaseModel, Field
import psycopg2
from fastapi.responses import HTMLResponse
from fastapi import Depends
from fastapi.templating import Jinja2Templates
from uuid import UUID
from POSTGRES.database import engine, sessionlocal
from POSTGRES import models
from sqlalchemy.orm import Session
import requests
from fastapi.responses import RedirectResponse


app = FastAPI()

templates =Jinja2Templates(directory="templates")

models.Base.metadata.create_all(bind=engine)

DATABASE_URL = "postgresql://postgres:root@postgresdb/postgres"

def get_connection():
    db =sessionlocal()
    try:
        yield db
    finally:
        db.close()
    print("May - postgres connected")


class Book(BaseModel):
    id: int
    title: str=Field(min_length=1)
    author: str=Field(min_length=1, max_length=100)    

BOOKS =[]

@app.get("/")
def read_api(request:Request, db: Session = Depends(get_connection)):
    books = db.query(models.Books).all()

    accept_header = request.headers.get("Accept", "")
    if "text/html" in accept_header:
        return templates.TemplateResponse("books.html", {"request": request, "books": books}, media_type="text/html")
    else:
        return {"request": "GET", "books": books}



@app.post("/")
def create_book(book:Book, db: Session = Depends(get_connection)):
    book_model=models.Books()
    book_model.id = book.id
    book_model.auther = book.author
    book_model.title = book.title

    db.add(book_model)
    db.commit()

    return book


@app.put("/{book_id}")
def update_book(book_id: int, book: Book, db: Session=Depends(get_connection)):

    book_model=db.query(models.Books).filter(models.Books.id == book_id).first()

    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID{book_id}: does not exist"
        )
    
    book_model.title = book.title
    book_model.auther=book.author

    db.add(book_model)
    db.commit()

@app.delete("/{book_id}")
def delete_book(book_id: int, book: Book, db: Session=Depends(get_connection)):
    
  
    book_model=db.query(models.Books).filter(models.Books.id==book_id).first()


    if book_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"ID{book_id}: does not exist"
        )
    
    db.query(models.Books).filter(models.Books.id==book_id).delete()
    db.commit()


@app.get("/Books-shop")
def redirecting():
    return RedirectResponse ("http://localhost:8501/")



# @app.get("/favicon.ico")
# def ignore_favicon():
#     return {"message": "Ignoring favicon request"}

# STREAMLIT_HOST = "localhost"
# @app.get("/books-shop")
# def trigger_streamlit_ui():
#     try:
#         # Make a request to the Streamlit UI endpoint using the service name
#         response = requests.get(f"http://{STREAMLIT_HOST}:8501/")
#         response.raise_for_status()  # Raise an exception for non-200 status codes
#         return {"message": "Streamlit UI triggered successfully"}
#     except requests.ConnectionError:
#         raise HTTPException(status_code=503, detail="Failed to connect to Streamlit UI server")
#     except requests.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Failed to trigger Streamlit UI: {str(e)}")


# class Item(BaseModel):
#     name: str
#     description: str


# @app.get("/")
# def index():
#     return {"greeting": "Hello, everything is up and running!"}

# @app.get("/index", response_class=HTMLResponse)
# def index2(request: Request):
#     clothes= [
#             {'name':'tshirt', 'size':'S'}
#     ]

#     context={'request': request, 'clothes':clothes}
#     return templates.TemplateResponse("index.html", context)

        # user = 'postgres', password='root', host='172.17.0.2', port='5432')




# from models import RequestBody, ResponseBody




# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.get('/colors') )
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.post("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     return {"item_id": item_id}

# async def get_shop_html():
#     with open(f".\\frontend\\may_shop.html", "r") as file:
#         return file.read()





# @app.post("/items/{item_id}")
# def create_item(item: dict, connection: psycopg2.extensions.connection = Depends(get_connection)):
#     try:
#         with connection.cursor() as cursor:
#             insert_query = "INSERT INTO items (name, description) VALUES (%s, %s) RETURNING id;"
#             cursor.execute(insert_query, (item["name"], item["description"]))
#             item_id = cursor.fetchone()[0]
#             connection.commit()
#             return {"id":item_id, **item}
        
#     except Exception as e:
#             raise NameError   

    





# @app.post("/dot")