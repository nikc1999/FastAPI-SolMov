
from datetime import datetime

from typing import Text, Union, Optional

from fastapi import FastAPI
from pydantic import BaseModel

from uuid import uuid4 as uuid
# Modelo de Noticia
class Noticia(BaseModel):
    id : str
    title : str
    author: str
    content: Text
    created_at: datetime = datetime.now()
    published_at: Optional[datetime]   #opcional
    published: bool = False

lista_noticias = []

app = FastAPI()

students = {
    1: {
        "name": "john",
        "age": 17,
        "class": "year 12"
    },
    2: {
        "name": "Alise",
        "age": 23,
        "class": "year 10"
    }
}

@app.get("/")
def read_root():
    return {"Hello": "Worldsdasd"}



@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id-1]


@app.get("/noticias")
def get_noticias():
    return lista_noticias




@app.post("/noticias")
def save_noticia(noticia : Noticia):
    noticia.id = str(uuid())
    print(noticia.dict())
    lista_noticias.append(noticia.dict())
    return "Noticia Cargada"

