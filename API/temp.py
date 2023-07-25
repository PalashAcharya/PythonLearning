import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import urllib
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException

app = FastAPI()
cnx = urllib.parse.quote_plus(
    'Data Source Name=MssqlDataSource;'
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=LAPTOP-I39M40T2\SQLEXPRESS;'
    'Database=Students;'
    'Trusted_connection=yes;'
)
try:
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(cnx))
    print("passed")
except:
    print("failed")

Sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)
Session = Sessionlocal()
Base = declarative_base()

class Student(Base):
    __tablename__ = "StudentData"
    ID = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Phone = Column(String)
    Area = Column(String)

class Studentpy(BaseModel):
    ID:int
    Name:str
    Phone:str
    Area:str
    class Config:
        orm_mode = True

@app.get("/Get")
def getdata():
    students = Session.query(Student).all();
    return students

@app.post("/Add",response_model=Studentpy)
async def AddStudent(s1:Studentpy):
    new_student = Student()
    new_student.Name = s1.Name
    new_student.Phone = s1.Phone
    new_student.Area = s1.Area
    Session.add(new_student)
    Session.commit()
    Session.refresh(new_student)
    s2 = Studentpy
    s2.ID = new_student.ID
    s2.Name = new_student.Name
    s2.Phone = new_student.Phone
    s2.Area = new_student.Area
    return s2