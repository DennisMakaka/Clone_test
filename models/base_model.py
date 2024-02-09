#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
    """Save the state of the object to the data store.

    This method updates the object's ``updated_at`` attribute with the current
    date and time, and then saves the object to the data store by calling the
    ``save`` method of the ``Storage`` class.

    Returns:
        None
    """
    self.updated_at = datetime.today()
    models.storage.save()

    def to_dict(self):
        def to_dict(self):
            """Return the dictionary of the BaseModel instance.
        
            Includes the key/value pair __class__ representing
            the class name of the object.
            """
            rdict = self.__dict__.copy()
            rdict["created_at"] = self.created_at.isoformat()
            rdict["updated_at"] = self.updated_at.isoformat()
            rdict["__class__"] = self.__class__.__name__
            return rdict
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        def __str__(self):
                """Return the print/str representation of the BaseModel instance.
        
                Returns:
                    str: The print/str representation of the BaseModel instance.
                """
                clname = self.__class__.__name__
                return f"[{clname}] ({self.id}) {self.__dict__}"
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)

