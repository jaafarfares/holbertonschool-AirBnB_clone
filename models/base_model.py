#!/usr/bin/python3
"""this is the base module """

import uuid
from datetime import datetime
import models


class BaseModel:
    """ the class basemodule """
    def __init__(self, *args, **kwargs):

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the time ana save into the storage """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return the dict representation"""

        dict = self.__dict__.copy()
        dict["__class__"] = type(self).__name__
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        return dict
