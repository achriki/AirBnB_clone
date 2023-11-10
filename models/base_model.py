#!/usr/bin/pyhton3
"""Defines the BaseModel class."""
import uuid
from models import storage
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
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for k, v in kwargs:
                if k == "created_at" or k == "updated_at":
                    self.__dic__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdict = self.__dict__.copy()
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['__class__'] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) ({})".format(class_name, self.id, self.__dic__)
