import cmd

"""access the class Cmd for inheritance"""

class MyConsole(cmd.Cmd):
    prompt = ">>> "
    
    def do_ls(self, args):
        print("no contents currently")
    def do_quit(self, args):
        return True
#aliasing (using two commands for same purpose.eg: passing the quit function to a variable exit)
    do_exit = do_quit
MyConsole().cmdloop()
