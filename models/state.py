#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy import Column, Integer, String, DateTime, func
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    city_names = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        city_list = []
        for city in self.city_names:
            if city.state.id == self.id:
                city_list.append(city)
        return city_list
