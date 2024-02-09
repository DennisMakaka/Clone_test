#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """The basemodel of the HBnB project"""

    def __init__(self, *args, **kwargs):
        """ initializing the BaseModel
        Args:
            *args (any): undefined number of arguments
            **kwargs: key value pairs of arguments
        """

        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            if key == "__class__":
                pass
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, timeformat))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
    
    def save(self):
        """Update the public instance attribute 'updated_at' with the current datetime."""
        self.updated_at = datetime.today()

    def to_dict(self):
        """Return a dictionary containing all keys/values 
        of __dict__ of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_copy
    def __str__(self):
        """Return a string representation of the instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
        
                                    



