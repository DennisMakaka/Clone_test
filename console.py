#!/usr/bin/python3
"""Defines the HBnB console."""
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

class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        pass

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        pass

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        pass

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        pass

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program at end of file."""
        print("")
        return True
    
    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it to the JSON file, and prints the id.
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
