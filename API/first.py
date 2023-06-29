from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base
import urllib

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
    Name = Column(String)
    Phone = Column(String)
    Area = Column(String)

@app.get("/")
async def root():
    students = session.query(Student).all();
    return students

@app.get("/Getbyname/")
async def getbyname(name:str):
    student = session.query(Student).filter(Student.Name==name).all()
    return student

@app.get("/{id}")
async def GetwithId(id:int):
    student = session.query(Student).filter(Student.ID==id).first();
    return student

@app.get("/home")
async def greet():
    return {"Message":"Greetings"}