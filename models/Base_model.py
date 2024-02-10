#!/usr/bin/python3
import uuid
from datetime import datetime


classBaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self):
        """Initializes BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at attribute with current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns dictionary representation of BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
