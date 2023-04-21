#!/usr/bin/python3
"""
This module defines a class to manage storage of hbnb models in MySQL database.
"""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    This class handles storage of objects in a MySQL database using SQLAlchemy.

    Attributes:
        __engine: An instance of SQLAlchemy's Engine
        __session: An instance of SQLAlchemy's Session
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a new instance of the DBStorage class.

        Creates the engine and links it to the MySQL database using
        the environment variables:
        HBNB_MYSQL_USER
        HBNB_MYSQL_PWD
        HBNB_MYSQL_HOST
        HBNB_MYSQL_DB.
        If the environment variable HBNB_ENV is set to 'test',
        all tables in the database are dropped.
        The engine is created with the option
        pool_pre_ping=True for automatic
        checking of liveness before each use.
        """
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db_name = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, db_name),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Queries the current database session for all
        objects of the given class name or all classes if cls is None.
        Args:
            cls: A class object representing the type of objects to query.
            If None, query all types of objects.

        Returns:
            A dictionary with keys in the format
            '<class-name>.<object-id>' and values as the corresponding objects.
        """
        if cls is None:
            objs = self.__session.query(State).all()
            for model in [City, User, Place, Review, Amenity]:
                objs.extend(self.__session.query(model).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """
        Adds the object to the current database session.
        Args:
            obj: An instance of a class that inherits from BaseModel.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session obj if not None.
        Args:
            obj: An instance of a class that inherits from BaseModel.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database and the current database session.
        """
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """
        Close the session
        """
        self.__session.close()
