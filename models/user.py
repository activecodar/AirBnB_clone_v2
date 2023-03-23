#!/usr/bin/python3
"""
This module defines a class User model for the database
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """
    User class inherits from BaseModel and Base and defines
    attributes for a user object in the database
    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship("Place", backref="user", cascade="all, delete")
