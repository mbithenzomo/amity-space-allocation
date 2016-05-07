#!/usr/bin/env python
"""
Usage:
    amity create_room (Living|Office) <room_name>...
    amity add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]
    amity reallocate_person <person_identifier> <new_room_name>    
    amity load_people
    amity print_allocations [-o=filename]
    amity print_unallocated [-o=filename]
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
from docopt import docopt, DocoptExit
from models.rooms import Room
from models.persons import Person

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

            print('You have entered an invalid command.')
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

    def introduction():
        c = ''
        h = ' '
        v = ' '


        print c + "-" * 78 + c

        print "        db         88b           d88  88  888888888888  8b        d8 ".center(78, h) + c
        print "       d88b        888b         d888  88       88        Y8,    ,8P  ".center(78, h) + c
        print "      d8``8b       88`8b       d8`88  88       88         Y8,  ,8P   ".center(78, h) + c
        print "     d8`  `8b      88 `8b     d8` 88  88       88          `8aa8`    ".center(78, h) + c
        print "    d8YaaaaY8b     88  `8b   d8`  88  88       88           `88`     ".center(78, h) + c
        print "  d8`        `8b   88    `888`    88  88       88            88      ".center(78, h) + c
        print " d8`          `8b  88     `8`     88  88       88            88      ".center(78, h) + c


        print c + "-" * 78 + c
        print c + "Welcome to Amity Space Allocation!".center(78, h) + c
        print c + "-" * 78 + c
        print v + "ROOM ALLOCATION COMMANDS".center(78) + v
        print c + "-" * 78 + c
        print v + "1 - create_room (Living|Office) <room_name>...".center(78) + v
        print v + "2 - add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]".center(78) + v
        print v + "3 - reallocate_person <person_identifier> <new_room_name>".center(78) + v
        print v + "4 - load_people".center(78) + v
        print v + "5 - print_allocations [-o=filename]".center(78) + v
        print v + "6 - print_unallocated [-o=filename]".center(78) + v
        print v + "6 - print_room <room_name>".center(78) + v
        print v + "7 - save_state [--db=sqlite_database]".center(78) + v
        print v + "8 - load_state <sqlite_database>".center(78) + v
        print c + "-" * 78 + c
        print v + "OTHER COMMANDS".center(78) + v
        print c + "-" * 78 + c
        print v + "1 - help".center(78) + v
        print v + "2 - quit".center(78) + v
        print v + "3 - exit".center(78) + v

    intro = introduction()
    prompt = '(amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (Living|Office) <room_name>..."""
        Room().create_room(args)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]"""
        Person().add_person(args)

    def do_quit(self, arg):
        """Quits out of the interactive mode"""

        print 'Goodbye!'
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Interactive().cmdloop()

print(opt)