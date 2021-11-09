#!/usr/bin/python3
"""module of BaseModel class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ BaseModel """

    def __init__(self):
        """class constructor"""
        self.id = str(uuid4())
        self.updated_at = datetime.now()
        self.created_at = datetime.now()

    def __str__(self):
        """ STR method for BaseModel"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                self.id, self.__dict__))

    def to_dict(self):
        """ Dictionary containing keys/values """
        dict_ = dict(self.__dict__)
        dict_.update({"__class__": self.__class__.__name__,
                           "created_at": str(((self.created_at).isoformat())),
                           "updated_at": str(((self.updated_at).isoformat()))})
        return dict_

    def save(self):
        """Updates with the datetime"""
        self.updated_at = datetime.now()
