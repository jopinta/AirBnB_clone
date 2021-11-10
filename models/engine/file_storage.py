#!/usr/bin/python3

""" FileStorage Module """

from models.base_model import BaseModel
import json

class FileStorage():
    """ FileStorage class """

    __objects = {}
    __file_path = "file.json"

    def all(self):
        """Returns the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """ Set de object with the key """
        id = str(obj.id)
        newObj = str(obj.__class__.__name__)
        keyValue = newObj + "." + id
        FileStorage.__objects[keyValue] = obj


    def save(self):
        """ Serializes objets to JSON file"""
        dictionary_tmp = {}
        for key in FileStorage.__objects:
            dictionary_tmp[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w") as FileObj:
            json.dump(dictionary_tmp, FileObj)

    
    def reload(self):
        """ Deserializes the  JSON file """
        try:
            with open(FileStorage.__file_path, "r") as FileJSON:
                JSON = json.load(FileJSON)
            for key, value in JSON.items():
                self.__objects[key] = BaseModel(**value)
        except:
            pass