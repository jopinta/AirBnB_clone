#!/usr/bin/python3

""" FileStorage Module """

from models.base_model import BaseModel
import json
from models.user import User

model = {"BaseModel": BaseModel}


class FileStorage():
    """ FileStorage class """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, obj):
        """ Set de object with the key """
        id = str(obj.id)
        newObj = str(obj.__class__.__name__)
        keyValue = newObj + "." + id
        self.__objects[keyValue] = obj

    def save(self):
        """ Serializes objets to JSON file"""
        dictionary_tmp = {}
        for key in self.__objects:
            dictionary_tmp[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(dictionary_tmp, file)

    def reload(self):
        """ Deserializes the  JSON file """
        try:
            with open(self.__file_path, "r") as file:
                j = json.load(file)
            for key, value in j.items():
                self.__objects[key] = BaseModel(**value)
        except Exception:
            pass
