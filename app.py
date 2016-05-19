#!/usr/bin/env python
"""
Usage:
    amity create_room (Living|Office) <room_name>...
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    amity reallocate_person <employee_id> <new_room_name>
    amity load_people <filename>
    amity print_allocations [--o=filename.txt]
    amity print_unallocated [--o=filename.txt]
    amity print_room <room_name>
    amity save_state [--db=sqlite_database]
    amity load_state <sqlite_database>
    amity (-i | --interactive)

Options:
    -h --help     Show this screen.
    -i --interactive  Interactive Mode
    -v --version
"""

import sys
import cmd
from termcolor import cprint
from pyfiglet import figlet_format
from docopt import docopt, DocoptExit
from models import my_amity
from models.amity import spacer, border
from db.database import Database
from colorama import init
init(strip=not sys.stdout.isatty())

my_database = Database(my_amity)


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # Thrown when args do not match

            print("You have entered an invalid command!")
            print(exit)
            return

        except SystemExit:
            # Prints the usage for --help

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Interactive (cmd.Cmd):

    cprint(figlet_format('AMITY', font='univers'), 'cyan', attrs=['bold'])

    def introduction():
        print border
        print spacer
        print "WELCOME TO AMITY SPACE ALLOCATION!".center(70)
        print spacer
        print "ROOM ALLOCATION COMMANDS:".center(70)
        print spacer
        print "1. create_room (Living|Office) <room_name>...".center(70)
        print "2. add_person " \
            "< first_name> <last_name> (Fellow|Staff) " \
            "[<wants_space>]".center(70)
        print "3. reallocate_person <employee_id> <new_room_name>".center(70)
        print "4. load_people <filename>".center(70)
        print "5. print_allocations [--o=filename.txt]".center(70)
        print "6. print_unallocated [--o=filename.txt]".center(70)
        print "7. print_room <room_name>".center(70)
        print "8. save_state [--db=sqlite_database]".center(70)
        print "9. load_state <sqlite_database>".center(70)
        print spacer
        print "OTHER COMMANDS:".center(70)
        print spacer
        print "1. help".center(70)
        print "2. quit".center(70)
        print spacer
        print border

    intro = introduction()
    prompt = "(amity) "

    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (Living|Office) <room_name>..."""
        my_amity.create_room(args)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: \
        add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]"""
        my_amity.add_person(args)

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <employee_id> <new_room_name>"""
        my_amity.reallocate_person(args)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_people <filename>"""
        my_amity.load_people(args)

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [--o=filename.txt]"""
        my_amity.print_allocations(args)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--o=filename.txt]"""
        my_amity.print_unallocated(args)

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        my_amity.print_room(args)

    @docopt_cmd
    def do_save_state(self, args):
        """Usage: save_state [--db=sqlite_database]"""
        my_database.save_state(args)

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: load_state <sqlite_database>"""
        my_database.load_state(args)

    def do_quit(self, arg):
        """Quits out of the interactive mode"""
        print spacer
        print "Goodbye!"
        print spacer
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt["--interactive"]:
    Interactive().cmdloop()

print(opt)
