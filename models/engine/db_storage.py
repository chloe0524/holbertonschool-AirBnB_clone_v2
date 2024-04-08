#!/usr/bin/python3
"""Manage storage for hbnb clone v2"""

from os import getenv
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base


class DBStorage:
    """Manages storage of hbnb models in MySQL"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage"""
        mysql_user = getenv('HBNB_MYSQL_USER')
        mysql_pwd = getenv('HBNB_MYSQL_PWD')
        mysql_host = getenv('HBNB_MYSQL_HOST', 'localhost')
        mysql_db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(mysql_user, mysql_pwd, mysql_host,
                                             mysql_db),
                                      pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                        expire_on_commit=False))

    def all(self, cls=None):
        """Get all objs"""
        storage = {}
        class_storage_bdd = [User, State, City, Amenity, Place, Review]

        if cls is None:
            target_classes = class_storage_bdd
        else:
            target_classes = [cls] if cls in class_storage_bdd else []

        for cls in target_classes:
            for instance in self.__session.query(cls):
                key = "{}.{}".format(cls.__name__, instance.id)
                storage[key] = instance

        return storage

    def new(self, obj):
        """Adds new object to storage session"""
        self.__session.add(obj)

    def save(self):
        """Save all changes of the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database + current database session"""
        Base.metadata.create_all(self.__engine)

    def close(self):
        """close session"""
        self.__session.close()
