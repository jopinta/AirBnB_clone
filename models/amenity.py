#!/usr/bin/python3
"""class that inherit from BaseModel
"""

from models.base_model import BaseModel


class Amenity(BaseModel):

    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor"""
        super().__init__()
