#!/usr/bin/python3
"""Test for console"""

import unittest
import pep8
import os
import console
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """ test console"""

    @classmethod
    def setUpClass(cls):
        """Setup  test"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """dgvn"""
        del cls.console

    def tearDown(self):
        """dffdsfglt"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_emptyline(self):
        """empty line """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """ quit """
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())



if __name__ == "__main__":
    unittest.main()
