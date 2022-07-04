#!/usr/bin/python3
""" this is a comment """


from models.base_model import BaseModel


class Review(BaseModel):
    """ this is the class review """

    text = ""
    place_id = ""
    user_id = ""
