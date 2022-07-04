#!/usr/bin/python3
""" this is a comment """

from models.base_model import BaseModel


class User(BaseModel):
    """  this is another comment """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
