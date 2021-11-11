#!/usr/bin/python3
""" entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
import sys

class HBNBCommand(cmd.Cmd):
    """class definition"""

    prompt =  "(hbnb) "
    def do_quit(self, arg):
        """Quit command to exit the program
"""
        return 1

    def do_EOF(self):
        """end of file exit
"""
        return 1

    def do_create(self, arg):
        """reates a new instance"""
        args = arg.split(" ")
        if args == 0:
            print ("** class name missing **")
        if args[0] == "BaseModel":
            instancia = BaseModel()
            instancia.save()
            print (instancia.id)
        else:
            print ("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
