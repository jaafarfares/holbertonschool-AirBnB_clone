#!/usr/bin/python3
"""this is the base module """

import uuid
from datetime import datetime


class BaseModel:
    """ the class basemodule """
    def __init__(self, *args, **kwargs):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the time ana save into the storage """
        self.updated_at = datetime.now()

    def to_dict(self):
        """return the dict representation"""

        return self.__dict__
    
