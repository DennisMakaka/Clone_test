#!/usr/bin/python3
"""Command interpreter module for HBNB project."""

import cmd
import re
from shlex import split
from models.engine import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """
    This function takes in a string argument and returns a list of arguments.
    If the argument contains curly braces,
    If the argument contains square brackets,
    If neither of these are present, it will split the argument on commas.
    """
    curly_braces = re.search(r"\{(.*?)}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        "Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("") # Print a newline before exiting
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def help_quit(self):
        "Print help message for quit command."""
        print("Quit command to exit the program.")

    def help_EOF(self):
        """Print help message for EOF command."""
        print("EOF command to exit the program.")

    def help_help(self):
        """Print help message for help command."""
        print("Help command to get information about commands.")

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file,
        and prints the id.
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class name and id.
        Usage: show <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            del models.storage.all()[key]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name.
        Usage: all [<class name>]
        """
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        try:
            print([str(obj) for obj in objects.values()
                   if obj.__class__.__name__ == arg])
        except KeyError:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        try:
            if args[0] not in models.storage.all():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
                return
            if len(args) < 4:
                print("** attribute name missing **")
                return
            if len(args) < 5:
                print("** value missing **")
                return
            setattr(models.storage.all()[key], args[2], args[3])
            storage.save()
        except KeyError:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
