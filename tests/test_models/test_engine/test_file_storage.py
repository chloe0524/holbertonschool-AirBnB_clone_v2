#!/usr/bin/python3
""" tests 'file_storage'"""
import unittest
from models.base_model import BaseModel
from models import storage
import os


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        """ Remove storage file at end of tests """
        try:
            os.remove('file.json')
        except:
            pass

    def test_obj_list_empty(self):
        """ __objects is initially empty """
        self.assertEqual(len(storage.all()), 0)

    def test_new_and_all(self):
        """ New object is correctly added to __objects and __objects is properly returned """
        new = BaseModel()
        for obj in storage.all().values():
            temp = obj
        self.assertTrue(temp is obj)
        temp = storage.all()
        self.assertIsInstance(temp, dict)

    def test_base_model_init_save(self):
        """ save data to file """
        new = BaseModel()
        self.assertFalse(os.path.exists('file.json'))
        thing = new.to_dict()
        new.save()
        self.assertNotEqual(os.path.getsize('file.json'), 0)

    def test_reload(self):
        """loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_reload_from_nonexistent_and_empty(self):
        """ if file does not exist load from an empty file """
        self.assertEqual(storage.reload(), None)
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_key_format(self):
        """ Key formatted """
        new = BaseModel()
        _id = new.to_dict()['id']
        for key in storage.all().keys():
            temp = key
        self.assertEqual(temp, 'BaseModel' + '.' + _id)

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = FileStorage()

    @classmethod
    def teardown(cls):
        """tear"""
        del cls.user

    def test_new_user(self):
        """cgsb"""
        storage = FileStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Chloe"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])

    def test_reload_file_storage(self):
        """tests 'Reload'"""
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        with open(path, 'r') as f:
            lines = f.readlines()
        try:
            os.remove(path)
        except:
            pass
        self.storage.save()
        with open(path, 'r') as f:
            lines2 = f.readlines()
        self.assertEqual(lines, lines2)
        try:
            os.remove(path)
        except:
            pass
        with open(path, "w") as f:
            f.write("{}")
        with open(path, "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()