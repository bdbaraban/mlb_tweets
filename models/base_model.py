#!/usr/bin/env python3
"""Defines the BaseModel class."""
from datetime import datetime


class BaseModel:
    """Represents the base MLB Tweets class.

    Attributes:
        updated_at (datetime): The time of last update.
    """

    updated_at = datetime

    def __init__(self, **kwargs):
        """Initialize a new Team.

        Args:
            **kwargs (any): Key/value pairs of attributes.
        """
        for key, value in kwargs.items():
            if key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)

    def to_dict(self):
        """Return a dictionary representation of the Team instance."""
        d = self.__dict__.copy()
        d["updated_at"] = self.updated_at.isoformat()
        return d
