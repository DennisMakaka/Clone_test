#!/usr/bin/python3
import uuid
from datetime import datetime


classBaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self):
        """Initializes BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            models.storage.new(self)
<<<<<<< HEAD

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
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
    

    def __str__(self):
        """Return the print/str representation of the BaseModel instance.

        Returns:
            str: The print/str representation of the BaseModel instance.
        """
        clname = self.__class__.__name__
        return f"[{clname}] ({self.id}) {self.__dict__}"
       
=======
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Returns string representation of BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
>>>>>>> 8d2d26aaae9c35191eb4a8c918e790f7e9a985dc

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
