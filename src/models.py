import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    favorites_id = Column(Integer, primary_key=True)
    favorite_character_id = Column(Integer, ForeignKey('characters.character_id'))
    favorite_planet_id = Column(Integer, ForeignKey('planets.planet_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    user = relationship(User)

    def to_dict(self):
        return {}


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    character_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
