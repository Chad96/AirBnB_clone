#!/usr/bin/python3
"""[module/review module]"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
