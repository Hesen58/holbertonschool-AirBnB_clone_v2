#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv("HBNB_TYPE_STORAGE") == "db":
    storagedb = DBStorage()
    storagedb.reload()
else:
    storagefile = FileStorage()
    storagefile.reload()
