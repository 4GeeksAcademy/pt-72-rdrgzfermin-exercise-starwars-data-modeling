import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

    

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)
    username = Column(String(100), unique=True, nullable=False)

    planet = relationship('planet', back_populates="user")
    character = relationship('character', back_populates="user")
    favorites = relationship('Favorites', back_populates="user")

    def to_dict(self):
        return {}

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    eye_color = Column(String(255))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    terrain = Column(Integer)
    diameter = Column(Integer)
    population = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
