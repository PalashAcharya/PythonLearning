from pydantic import BaseModel, Field
from typing import Optional
from fastapi import FastAPI

app = FastAPI()

class Students(BaseModel):
    ID:int 
    Name:str = Field(examples = "palash")
    Phone:str | None = Field(default=None,title="The phone number of student",max_length=10,description="The phone number should be 10 digits only",examples="8200087138" )
    Area:str = Field(examples="Bodakdev")
data = {}

@app.post("/Add/{id}")
def Create_student(id:int,student:Students):
    data[id] = student
    return data[id]

@app.get("/Get")
def Getdata():
    return data