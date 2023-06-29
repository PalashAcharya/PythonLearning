from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

class Students(BaseModel):
    ID:int
    Name:str
    Phone:Optional[str] = None
    Area:str
data = {}

@app.post("/Add/{id}")
def Create_student(id:int,student:Students):
    data[id] = student
    return data[id]

@app.get("/Get")
def Getdata():
    return data