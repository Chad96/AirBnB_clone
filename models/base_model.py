#!/usr/bin/python3
"""[Base model module for HBnB Holberton's project]"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class for the HBnB"""

    def __init__(self, *args, **kwargs) -> None:
        """initializing a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """Returns:a strings with changed information"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the update_date"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns an specific information about the class in a dictionary"""
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
