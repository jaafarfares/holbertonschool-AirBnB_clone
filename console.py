#!/usr/bin/python3
""" this Module contains the entry point of the command interpreter """

import cmd
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

    def empyy_line(self, args):
        """ if no argument given """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
