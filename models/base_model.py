#!/usr/bin/python3
"""module of BaseModel class"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ BaseModel """

    def __init__(self, *args, **kwargs):
        """class constructor"""
        date = "%Y-%m-%dT%H:%M:%S.%f"

        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    res = datetime.strptime(value, date)
                if key != "__class__":
                    setattr(self, key, res)

    def __str__(self):
        """ STR method for BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def to_dict(self):
        """ Dictionary containing keys/values """
        dicc = dict(self.__dict__)
        dicc.update({"__class__": self.__class__.__name__,
                     "created_at": str(((self.created_at).isoformat())),
                     "updated_at": str(((self.updated_at).isoformat()))})
        return dicc

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        models.storage.save()