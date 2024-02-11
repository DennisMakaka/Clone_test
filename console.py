#!/usr/bin/python3
"""Command interpreter module for HBNB project."""

import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
