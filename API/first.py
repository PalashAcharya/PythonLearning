from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
import urllib
from pydantic import BaseModel
import pyodbc

app  = FastAPI()
conn = urllib.parse.quote_plus(
    'Data Source Name=MssqlDataSource;'
    'Driver={ODBC Driver 17 for SQL Server};'
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

class studentpy(BaseModel):
    ID : int
    Name : str
    Phone: str
    Area: str
    class Config:
        orm_mode = True


class Student(Base):
    __tablename__ = "StudentData"
    ID = Column(Integer,primary_key=True,index=True)
    Name = Column(String)
    Phone = Column(String)
    Area = Column(String)


@app.post("/Add_Student/",response_model=studentpy)
async def add_student(student1:studentpy):
    new_person = Student()
    new_person.Name = student1.Name
    new_person.Phone = student1.Phone
    new_person.Area = student1.Area
    session.add(new_person)
    session.commit()
    session.refresh(new_person)
    s2 = studentpy.from_orm(new_person)
    return s2


@app.delete("/Delete_Student/{s_id}")
def Deletestudent(s_id:int):
    find_student = session.query(Student).filter(Student.ID==s_id).first();
    session.delete(find_student)
    session.commit()
    return find_student

@app.put("/UpdateStudent/{s_id}",response_model=studentpy)
async def UpdateStudent(s_id: int,student1:studentpy):
    find_student = session.query(Student).filter(Student.ID ==s_id).first();
    find_student.ID = student1.ID
    find_student.Name = student1.Name
    find_student.Area = student1.Area
    find_student.Phone = student1.Phone
    session.commit()
    session.refresh(find_student)
    s1 = studentpy
    s1.ID = find_student.ID
    s1.Name = find_student.Name
    s1.Area = find_student.Area
    s1.Phone = find_student.Phone
    return s1

@app.get("/")
async def root():
    students = session.query(Student).all();
    return students

@app.get("/Getbyname/{name}")
async def getbyname(name:str):
    student = session.query(Student).filter(Student.Name==name).all();
    return student

@app.get("/{id}")
async def GetwithId(id:int):
    student = session.query(Student).filter(Student.ID==id).first();
    return student

@app.get("/home")
async def greet():
    return {"Message":"Greetings"}