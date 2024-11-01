import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

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
    __planet__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    terrain = Column(String(255))
    diameter = Column(Integer)
    population = Column(Integer)

    def serialize(self):
        return {}

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    planet_id = Column(Integer, ForeignKey("planet.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    
    user = relationship("User", Column="favorites")
    planet = relationship("Planet", Column="favorites")
    character = relationship("Character", Column="favorites")

    def serialize(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
