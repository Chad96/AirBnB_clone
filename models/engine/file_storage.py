#!/usr/bin/python3
"""contains the FileStorage class in this module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """A class Engine to serialize to json and deserialize to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects of the dictionary"""
        return self.__objects

    def new(self, obj):
        """sets in objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialization"""
        dict_data = self.__objects
        transformed = {key: dict_data[key].to_dict()
                       for key, _ in dict_data.items()}
        with open(self.__file_path, mode="w") as f:
            json.dump(transformed, f)

    def reload(self):
        """deserializes from Json file"""
        try:
            with open(self.__file_path, mode="r") as f:
                readed = json.load(f)
            for _, dict_readed in readed.items():
                class_name = dict_readed.__getitem__('__class__')
                self.new(eval(class_name)(**dict_readed))
        except FileNotFoundError:
            return
