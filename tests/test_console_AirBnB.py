#!/usr/bin/python3
"""unitests for console methods"""
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Test cases for the HBNBCommand class"""

    def setUp(self):
        self.console = HBNBCommand()

    def test_do_quit(self):
        """Test that the do_quit method exits the program"""
        with patch('sys.exit') as mock_exit:
            self.console.do_quit(None)
            mock_exit.assert_called_once()

    def test_do_EOF(self):
        """Test that the do_EOF method prints an empty line"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_EOF(None)
            self.assertEqual(mock_output.getvalue().strip(), '')

    def test_emptyline(self):
        """Test that the emptyline method does nothing"""
        self.assertIsNone(self.console.emptyline())

    def test_do_creates_new(self):
        """Test that the do_create method creates a new instance"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_create('BaseModel')
            self.assertIn('BaseModel', mock_output.getvalue())

    def test_do_show_missing(self):
        """Test that the do_show method handles missing instances"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_show('BaseModel 6666')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_destroy_missing(self):
        """Test that the do_destroy method handles missing instances"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_destroy('BaseModel 6666')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_all_empty(self):
        """Test that the do_all method handles an empty class"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_all('BaseModel')
            self.assertIn('[]', mock_output.getvalue())

    def test_do_count(self):
        """Test that the do_count method counts instances correctly"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_count('BaseModel')
            self.assertIn('0', mock_output.getvalue())

    def test_do_updates_missing(self):
        """Test that the do_update method handles missing instances"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_update('BaseModel 6666 name
                                   "New Dog, hello Nestie"')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_updates(self):
        """Test that the do_update method updates an instance"""
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.onecmd('create BaseModel')
            instance_id = mock_output.getvalue().strip()
            self.console.onecmd('update BaseModel {} name
                                "New dog, hello Nestie"'.format(instance_id))
            self.console.onecmd('show BaseModel {}'.format(instance_id))
            self.assertIn('New dog, hello Nestie', mock_output.getvalue())


if __name__ == '__main__':
    unittest.main()
