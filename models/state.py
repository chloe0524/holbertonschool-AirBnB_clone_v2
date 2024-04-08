#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class + inheritance """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        city_list = []
        for city in FileStorage.all(City):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
