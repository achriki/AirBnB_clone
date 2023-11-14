#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        newKey = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[newKey] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, "w") as json_file:
            ser_objs = {
                key: obj.to_dict() for key, obj in self.__objects.items()
                }
            json.dump(ser_objs, json_file)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if os.path.exists(self.__file_path):
            with open(self.__file_path) as json_file:
                desr_objs = json.load(json_file)
                for obj in desr_objs.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
