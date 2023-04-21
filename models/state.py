#!/usr/bin/python3
""" State Module for HBNB project """
import os

from sqlalchemy import Column, String

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            from models import storage
            from models.city import City
            """
            Returns the list of City instances
            with state_id equals to the current State.id
            """
            return [c for c in storage.all(City).values()
                    if c.state_id == self.id and isinstance(c, City)]
