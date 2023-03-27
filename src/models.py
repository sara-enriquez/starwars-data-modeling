import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    last_name = Column(String(120))
    email = Column(String(250), nullable=False)
    user_name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    registration_date = Column (String(50))

class Character(Base):
    __tablename__='character'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    birth_year = Column(String(50))
    gender = Column(String(50))
    height = Column(String(50))
    skin_color = Column(String(50))
    eye_color = Column(String(50))

class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    climate = Column(String(120))
    population = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)

class Vehicle(Base):
    __tablename__='vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    description = Column(String(500), nullable=False)
    passengers = Column(Integer)
    model = Column(String(120))
    crew = Column(String(120))
    consumables = Column(String(120))
    cost = Column(Integer)

class Favs(Base):
    __tablename__ = 'favs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
