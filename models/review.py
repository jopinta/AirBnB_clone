#!/usr/bin/python3
"""class that inherit from BaseModel
"""

from models.base_model import BaseModel
import models

class Review(BaseModel):

    place_id = ""
    user_id = ""
    text = ""
