#!/usr/bin/python3
""" entry point of the command interpreter
"""
from shlex import split
import cmd
from models.base_model import BaseModel
import models
import sys

newdict = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """ Class definition """

    prompt =  "(hbnb) "
    def do_quit(self, argument):
        """ Quit command to exit the program """
        return 1

    def do_EOF(self):
        """ End of file exit """
        return 1

    def do_create(self, argument):
        """ Reates a new instance """
        args = split(argument)
        if (len(args)) == 0:
            print ("** class name missing **")
        elif args[0] == "BaseModel":
            instancia = BaseModel()
            instancia.save()
            print (instancia.id)
        else:
            print ("** class doesn't exist **")

    def do_show(self, argument):
        """ Prints the string representation """
        args = split(argument)
        if (len(args)) == 0:
            print ("** class name missing **")
        elif args[0] not in newdict:
            print ("** class doesn't exist **")
        else:
            if (len(args)) == 1:
                    print ("** instance id missing **")
            else:
                    element = args[0] + "." + args[1]
                    if str(element) in models.storage.all():
                            print (models.storage.all()[element])
                    else:
                            print("** no instance found **")
    

    def do_all(self, argument):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        args = split(argument)
        list = []
        if len(args) == 0:
            for values in models.storage.all().values():
                list.append(values.__str__())
        elif len(args) == 1:
            if args[0] not in newdict:
                print("** class doesn't exist **")
                return
            for key, values in models.storage.all().items():
                separador = key.split('.')
                if separador[0] == args[0]:
                    list.append(values.__str__())
        print(list)

    def emptyline(self):
        """ empty line """
        pass
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
