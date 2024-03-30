#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if not getenv("HBNB_TYPE_STORAGE") == "db":

        @property
        def cities(self):
            '''Something more useful'''
            lcities = []
            for i in list(storage.all(City).values()):
                if i.state_id == self.id:
                    lcities.append(i)
            return lcities
