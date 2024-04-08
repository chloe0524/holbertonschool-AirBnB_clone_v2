#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from models.city import City  # Import the City class
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', back_populates='state', cascade='all, delete')

    @property
    def cities(self):
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
