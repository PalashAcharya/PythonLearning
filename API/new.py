import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column,  Integer, String
from sqlalchemy.orm import sessionmaker
import urllib
from pydantic import  BaseModel

from fastapi import FastAPI, HTTPException

app  = FastAPI()
conn = urllib.parse.quote_plus(
    'Data Source Name=MssqlDataSource;'
    'Driver={SQL Server};'
    'Server=LAPTOP-I39M40T2\SQLEXPRESS;'
    'Database=Students;'
    'Trusted_connection=yes;'
)

try:

    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(conn))
    print("Passed")
except:
    print("failed!")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = SessionLocal()
class Student(Base):
    __tablename__ = "StudentData"

    ID = Column(Integer, primary_key=True, index=True)
    SName = Column(String)
    Area = Column(String)
    Phone = Column(String)

class StudentDB(BaseModel):
    ID:int
    SName:str
    Area:str|None
    Phone:str|None
    class Config:
        orm_mode=True

app = FastAPI()

@app.get("/student/", response_model=list[StudentDB])
async def getList():
    students = session.query(Student).all();
    return students

@app.get("/student/byid/{id}",response_model=StudentDB)
async def getById(id:int ):
    student = session.query(Student).filter(Student.ID==id).first();
    print(student)
    s1 = StudentDB.from_orm(student)
    print(s1)
    return s1

@app.get("/student/byname/{sname}",response_model=list[StudentDB])
async def getByName(sname:str):
    students = session.query(Student).filter(Student.SName==sname).all();
    # print(student)
    # s1 = StudentDB.from_orm(student)
    # print(s1)
    return students
# @app.get("/item")
# async def getItems():
#     return {"message": "From items"}

@app.post("/student/add", response_model=StudentDB)
async def addStudent(student:StudentDB):
    s1=Student() #Object of DB Model
    s1.SName= student.SName
    s1.Area = student.Area
    s1.Phone = student.Phone
    session.add(s1)
    session.commit()
    session.refresh(s1)
    result = StudentDB.from_orm(s1)
    return result
@app.put("/student/edit/{id}", response_model=StudentDB)
async def editStudent(id:int, student:StudentDB):
    s1 = session.query(Student).filter(Student.ID == id).first();
    if not s1:
        raise HTTPException(status_code=404, detail="Student not found")

    s1.SName= student.SName
    s1.Area=student.Area
    s1.Phone = student.Phone
    session.commit()
    session.refresh(s1)
    s2= StudentDB.from_orm(s1)
    return s2

@app.delete("/student/{id}")
def delete_student(id:int):
    s1 = session.query(Student).filter(Student.ID == id).first();
    if not s1:
        raise HTTPException(status_code=404, detail="Student not found")
    session.delete(s1)
    session.commit()
    return {"Ok":True}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)