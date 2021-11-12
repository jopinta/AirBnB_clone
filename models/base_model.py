#!/usr/bin/python3
"""module of BaseModel class"""

from datetime import datetime
import uuid
import models


class BaseModel():
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """Class constructor"""
        date = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.created_at = datetime.now()
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, date)
                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """ STR method for BaseModel"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Serializes objects to the JSON file """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Dictionary containing keys/values """
        dicc = dict(self.__dict__)
        dicc["created_at"] = self.created_at.isoformat()
        dicc["__class__"] = self.__class__.__name__
        dicc["updated_at"] = self.updated_at.isoformat()
        return dicc