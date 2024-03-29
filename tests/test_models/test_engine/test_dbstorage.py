#!/usr/bin/python3
"""tests file storage"""
import unittest
from unittest.mock import MagicMock, patch
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


class TestDBStorage(unittest.TestCase):
    '''DBStorage tests'''

    def setUp(self):
        """SetUp env for test"""
        pass

    def tearDown(self):
        """teardown"""
        pass

    def test_all(self):
        """all"""
        pass

    def test_all_with_class_argument(self):
        """test returns all objects of a class"""
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            user = User()
            self.storage.new(user)
            self.storage.save()
            all_users = self.storage.all(User)
            self.assertIn(user, all_users.values())

    def test_all_without_class_argument(self):
        """dsbdfb"""
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            user = User()
            state = State()
            city = City()
            self.storage.new(user)
            self.storage.new(state)
            self.storage.new(city)
            self.storage.save()
            all_objects = self.storage.all()
            self.assertIn(user, all_objects.values())
            self.assertIn(state, all_objects.values())
            self.assertIn(city, all_objects.values())

    def test_all_with_no_objects(self):
        """ghxto objects"""
        with patch('sys.stdout', new=MagicMock()) as mock_stdout:
            all_objects = self.storage.all()
            self.assertEqual(len(all_objects), 0)

    def test_new(self):
        """new """
        pass

    def test_save(self):
        """save"""
        pass

    def test_delete(self):
        """delete"""
        pass

    def test_reload(self):
        """reload"""
        pass

if __name__ == "__main__":
    unittest.main()