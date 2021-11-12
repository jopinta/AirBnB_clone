#!/usr/bin/python3
""" entry point of the command interpreter
"""

import cmd
from models.base_model import BaseModel
import sys
newdict = {}
args = []


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

    def do_show(self, arg):
        """Prints the string representation"""
        args = arg.split(" ")
        if (len(args)) == 0:
            print ("** class name missing **")
            return 0
        if args[0] not in newdict:
            print ("** class doesn't exist **")

            if (len(args)) == 1:
                    print ("")
        else:
                    element = arg[0] + "." + arg[1]
                    print (models.storage.all()[element])

if __name__ == '__main__':
    HBNBCommand().cmdloop()
