#!/usr/bin/python3
""" class FileStorage that serializes instances to a JSON file
and deserializes JSON file to instances:"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fstorobj = FileStorage.__objects
        objdict = {obj: fstorobj[obj].to_dict() for obj in fstorobj.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to __objects.
        (only if the JSON file (__file_path) exists"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f.read())
                new_dict = dict()

        except Exception:
            return
