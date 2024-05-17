#!/usr/bin/python3
"""This script is the base model"""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines all common attributes/methods for other classes.
    """

    def __init__(self):
        """
        Initialize BaseModel instance with id and timestamps.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Update the updated_at attribute to current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return dictionary representation of BaseModel instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
