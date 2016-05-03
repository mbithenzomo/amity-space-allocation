'''
Usage:
    amity.py allocate (-p <first_name> <last_name> -r <room_name>)
    amity.py unallocate (-p <first_name> <last_name> -r <room_name>)
    amity.py view-unallocated
    amity.py view-unallocated-fellows
    amity.py view-unallocated-staff
    amity.py view-occupants (<room_name>)
    amity.py view-unoccupied
    amity.py view-allocations

Options:
    -h --help     Show this screen.
'''

from docopt import docopt