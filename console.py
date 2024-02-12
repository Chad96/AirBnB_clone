#!/usr/bin/env python3
"""Console 0.1"""

import cmd
import json
import models
from models import classes


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty input line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = models.classes[arg]()
                new_instance.save()
                print(new_instance.id)
            except KeyError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(cls_name, instance_id)
                    all_instances = models.storage.all()
                    if key in all_instances:
                        print(all_instances[key])
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(cls_name, instance_id)
                    all_instances = models.storage.all()
                    if key in all_instances:
                        del all_instances[key]
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances"""
        args = arg.split()
        all_instances = models.storage.all()
        if not args:
            print([str(inst) for inst in all_instances.values()])
        else:
            try:
                cls_name = args[0]
                if cls_name in models.classes:
                    filtered_instances = [str(inst) for inst in all_instances.values() if inst.__class__.__name__ == cls_name]
                    print(filtered_instances)
                else:
                    print("** class doesn't exist **")
            except KeyError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                cls_name = args[0]
                if cls_name not in models.classes:
                    print("** class doesn't exist **")
                    return

                if len(args) > 1:
                    instance_id = args[1]
                    key = "{}.{}".format(cls_name, instance_id)
                    all_instances = models.storage.all()
                    if key in all_instances:
                        if len(args) > 2:
                            attribute_name = args[2]
                            if len(args) > 3:
                                attribute_value = args[3]
                                setattr(all_instances[key], attribute_name, eval(attribute_value))
                                models.storage.save()
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            except KeyError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
 