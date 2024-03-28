#!/usr/bin/python3
"""Unit tests for console methods"""
import unittest
import os
import io
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

    @classmethod
    def setUpClass(cls):
        """Set up test class"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down test class"""
        del cls.console

    def tearDown(self):
        """Remove temporary file (file.json) created during tests"""
        try:
            os.remove("file.json")
        except Exception:
            pass
    def create(self):
        """ Creates an instance of interpreter """
        return HBNBCommand()

    def test_create_normal(self):
        """ Test the create command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("create City")
            self.assertEqual(type(mock_stdout.getvalue()), str)

    def test_show(self):
        """ Test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("create City")
            city_id = mock_stdout.getvalue()
            console.onecmd("show City {}".format(city_id))
            self.assertIsInstance(mock_stdout.getvalue(), str)

    def test_show_errB(self):
        """ Test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("show")
            self.assertEqual(mock_stdout.getvalue(),
                             "** class name missing **\n")

        """ Test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("show City")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def test_show_errC(self):
        """ Test the show command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd("show Bla {}".format(city_id))
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_destroy_errA(self):
        """ Test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("destroy City")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def test_destroy_errB(self):
        """ Test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd("destroy Bla {}".format(city_id))
            self.assertEqual(mock_stdout.getvalue(),
                             "** class doesn't exist **\n")

    def test_destroy_errC(self):
        """ Test the destroy command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            city_id = mock_stdout.getvalue()
            console.onecmd("destroy {}".format(city_id))
            self.assertEqual(mock_stdout.getvalue(),
                             "** class name missing **\n")

    def test_all(self):
        """ Test the all command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd('create State name="Germany"')
            console.onecmd("all State")
            self.assertIn("Germany", mock_stdout.getvalue())

    def test_update_A(self):
        """ Test the update command """
        with unittest.mock.patch('sys.stdout',
                                 new_callable=io.StringIO) as mock_stdout:
            console = self.create()
            console.onecmd("update User")
            self.assertEqual(mock_stdout.getvalue(),
                             "** instance id missing **\n")

    def setUp(self):
        self.console = HBNBCommand()

    def test_do_quit(self):
        """ Test that the do_quit method exits the program """
        with patch('sys.exit') as mock_exit:
            self.console.do_quit(None)
            mock_exit.assert_called_once()

    def test_do_EOF(self):
        """ Test that the do_EOF method prints an empty line """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_EOF(None)
            self.assertEqual(mock_output.getvalue().strip(), '')

    def test_emptyline(self):
        """ Test that the emptyline method does nothing """
        self.assertIsNone(self.console.emptyline())

    def test_do_creates_new(self):
        """ Test that the do_create method creates a new instance """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_create('BaseModel')
            self.assertIn('BaseModel', mock_output.getvalue())

    def test_do_show_missing(self):
        """ Test that the do_show method handles missing instances """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_show('BaseModel 6666')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_destroy_missing(self):
        """ Test that the do_destroy method handles missing instances """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_destroy('BaseModel 6666')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_all_empty(self):
        """ Test that the do_all method handles an empty class """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_all('BaseModel')
            self.assertIn('[]', mock_output.getvalue())

    def test_do_count(self):
        """ Test that the do_count method counts instances correctly """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_count('BaseModel')
            self.assertIn('0', mock_output.getvalue())

    def test_do_updates_missing(self):
        """ Test that the do_update method handles missing instances """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.do_update('BaseModel 6666 name "New Dog, hello Nestie"')
            self.assertIn('** no instance found **', mock_output.getvalue())

    def test_do_updates(self):
        """ Test that the do_update method updates an instance """
        with patch('sys.stdout', new=StringIO()) as mock_output:
            self.console.onecmd('create BaseModel')
            instance_id = mock_output.getvalue().strip()
            self.console.onecmd('update BaseModel {} name "New dog, hello Nestie"'.format(instance_id))
            self.console.onecmd('show BaseModel {}'.format(instance_id))
            self.assertIn('New dog, hello Nestie', mock_output.getvalue())


if __name__ == '__main__':
    unittest.main()
