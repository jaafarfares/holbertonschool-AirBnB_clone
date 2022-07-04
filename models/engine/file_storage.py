#!/usr/bin/python3

import json


class FileStorage:
    __file_path = "file.json"
    __objects = ""

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        filee = FileStorage.__objects
        objdict = {obj: filee[obj].to_dict() for obj in filee.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f.read())
                new_dict = dict()

        except Exception:
            return  
