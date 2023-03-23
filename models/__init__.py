#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

from models.engine.file_storage import FileStorage


db_storage_env = os.getenv('HBNB_TYPE_STORAGE')

if db_storage_env == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
