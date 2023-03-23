#!/usr/bin/python3
"""
Place Module for HBNB project
"""
from sqlalchemy import Column, ForeignKey, String, Integer, Float

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class inherits from BaseModel and defines
    attributes for a place object
    Attributes:
        city_id (str): city id of the place
        user_id (str): user id of the place
        name (str): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms of the place
        number_bathrooms (int): number of bathrooms of the place
        max_guest (int): max number of guests of the place
        price_by_night (int): price by night of the place
        latitude (float): latitude of the place
        longitude (float): longitude of the place
    """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
