#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""

import unittest
import os
import models
from models.base_model import BaseModel
from datetime import datetime
from time import sleep
<<<<<<< HEAD

class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

=======

class TestBaseModel(unittest.TestCase):
    """Unittests for the BaseModel class."""

>>>>>>> b50bb5e2dfefd959e2bcc5b3b29dcd89e53283e1
    @classmethod
    def setUpClass(cls):
        """Setup class for the tests."""
        cls.bm = BaseModel()

    @classmethod
    def tearDownClass(cls):
        """Tear down class after the tests."""
        del cls.bm

    def test_instance_attributes(self):
        """Test instance attributes."""
        self.assertTrue(hasattr(self.bm, 'id'))
        self.assertTrue(hasattr(self.bm, 'created_at'))
        self.assertTrue(hasattr(self.bm, 'updated_at'))
        self.assertEqual(type(self.bm.id), str)
        self.assertEqual(type(self.bm.created_at), datetime)
        self.assertEqual(type(self.bm.updated_at), datetime)

    def test_str_representation(self):
        """Test string representation."""
        expected_str = "[BaseModel] ({}) {}".format(self.bm.id, self.bm.__dict__)
        self.assertEqual(str(self.bm), expected_str)

    def test_save_method(self):
        """Test save method."""
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method."""
        obj_dict = self.bm.to_dict()
        self.assertEqual(type(obj_dict), dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], self.bm.id)
        self.assertEqual(obj_dict['created_at'], self.bm.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], self.bm.updated_at.isoformat())

    def test_to_dict_method_with_args(self):
        """Test to_dict method with arguments."""
        with self.assertRaises(TypeError):
            self.bm.to_dict(None)

    def test_two_models_unique_ids(self):
        """Test unique IDs for two BaseModel instances."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_two_models_different_created_at(self):
        """Test different created_at times for two BaseModel instances."""
        bm1 = BaseModel()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_different_updated_at(self):
        """Test different updated_at times for two BaseModel instances."""
        bm1 = BaseModel()
        sleep(0.01)
        bm1.save()
        sleep(0.01)
        bm2 = BaseModel()
        self.assertLess(bm1.updated_at, bm2.updated_at)

    def test_save_method_with_argument(self):
        """Test save method with argument."""
        with self.assertRaises(TypeError):
            self.bm.save(None)

    def test_to_dict_method_output(self):
        """Test to_dict method output."""
        expected_dict = {
            '__class__': 'BaseModel',
            'id': self.bm.id,
            'created_at': self.bm.created_at.isoformat(),
            'updated_at': self.bm.updated_at.isoformat()
        }
        self.assertDictEqual(self.bm.to_dict(), expected_dict)

<<<<<<< HEAD
    def test_init_with_dict_representstion(self):
        """Test __init__ method with dictionary representstion."""
        bm_dict = self.bm.to.dict()
        bm_from_dict = BaseModel(**bm_dict)
        self.assertEqual(type(bm_from_dict), BaseModel)
        for key, value in bm_dict.items():
            if key != '__class__':
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    self.assterEqual(getattr(bm_from_dict, key), value)


if __name__ == "__main__":
    unittest.main()
=======

if __name__ == "__main__":
    unittest.main()

>>>>>>> b50bb5e2dfefd959e2bcc5b3b29dcd89e53283e1
