#!/usr/bin/python3
""" entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class definition"""

    def do_quit(self, arg):
        """Quit command to exit the program
"""
        return 1

    def do_EOF(self):
        """end of file exit
"""
        return 1
prompt = "(hbnb) "

if __name__ == '__main__':
    HBNBCommand().cmdloop()
