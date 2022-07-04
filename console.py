#!/usr/bin/python3
""" this Module contains the entry point of the command interpreter """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ the class HBNBCommand """
    prompt = '(hbnb) '

    def do_EOF(self, args):
        """ to exit the comand line"""
        print()
        return True

    def do_quit(self, args):
        """ to quit the promt"""
        return True

    def empyy_line(self):
        """ if no argument given """
        pass

    def do_help(self, args):
        """ help """
        cmd.Cmd.do_help(self, args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
