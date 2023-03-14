# I will use SQLite for this exercise 


#Data model to represent the weather data records

CREATE TABLE station (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE weather_record (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    max_temp INTEGER NOT NULL,
    min_temp INTEGER NOT NULL,
    precipitation INTEGER NOT NULL,
    station_id INTEGER NOT NULL,
    FOREIGN KEY(station_id) REFERENCES station(id)
);


#Data representation in python using ORM-SQLAlchemy in Python

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Define the base class for SQLAlchemy ORM models
Base = declarative_base()

# Define the Station model
class Station(Base):
    __tablename__ = 'station' 

    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False) 

# Define the WeatherRecord model
class WeatherRecord(Base):
    __tablename__ = 'weather_record' 

    id = Column(Integer, primary_key=True) 
    date = Column(String, nullable=False) 
    max_temp = Column(Integer, nullable=False) 
    min_temp = Column(Integer, nullable=False) 
    precipitation = Column(Integer, nullable=False) 
    station_id = Column(Integer, ForeignKey('station.id'), nullable=False) 
    station = relationship(Station) 

# Create the SQLite database
engine = create_engine('sqlite:///weather_data.db') 
Base.metadata.create_all(engine) 

# Set up a session to interact with the database
Session = sessionmaker(bind=engine) 
session = Session() 

