#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    """Unittests for testing FileStorage class."""

    def setUp(self):
        """Set up the test environment."""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down the test environment."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

    def test_save_reload(self):
        """Test the save and reload methods."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all())

if __name__ == "__main__":
    unittest.main()
