#!/usr/bin/env python3
"""Console module."""
import cmd
from models import storage
from models.base_model import BaseModel
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty input."""
        pass

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program."""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Show string representation of an instance."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = args[1]
                    key = "{}.{}".format(class_name, obj_id)
                    all_objs = storage.all()
                    if key in all_objs:
                        print(all_objs[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) < 2:
                    print("** instance id missing **")
                else:
                    obj_id = args[1]
                    key = "{}.{}".format(class_name, obj_id)
                    all_objs = storage.all()
                    if key in all_objs:
                        del all_objs[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints string representation of all instances."""
        args = arg.split()
        all_objs = storage.all()
        if not arg:
            print([str(all_objs[obj]) for obj in all_objs])
        else:
            try:
                class_name = args[0]
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    print([str(all_objs[obj]) for obj in all_objs if obj.startswith(class_name)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name not in storage.classes():
                    print("** class doesn't exist **")
                else:
                    if len(args) < 2:
                        print("** instance id missing **")
                    else:
                        obj_id = args[1]
                        key = "{}.{}".format(class_name, obj_id)
                        all_objs = storage.all()
                        if key not in all_objs:
                            print("** no instance found **")
                        else:
                            if len(args) < 3:
                                print("** attribute name missing **")
                            else:
                                attr_name = args[2]
                                if len(args) < 4:
                                    print("** value missing **")
                                else:
                                    attr_value = args[3]
                                    obj = all_objs[key]
                                    setattr(obj, attr_name, eval(attr_value))
                                    obj.updated_at = datetime.now()
                                    storage.save()
            except NameError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
