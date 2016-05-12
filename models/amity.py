import random
from rooms import Office, Living
from people import Staff, Fellow
from termcolor import colored

spacer = colored("-" * 70, 'cyan')


class Amity():
    def __init__(self):
        self.rooms = []
        self.offices = []
        self.vacant_offices = []
        self.livingspaces = []
        self.vacant_livingspaces = []
        self.people = []
        self.fellows = []
        self.assigned_fellows = []
        self.staff = []
        self.assigned_staff = []

    def create_room(self, args):
        """Create new room(s)"""
        print spacer
        new_rooms = []
        for room in args["<room_name>"]:
            if room.lower() in [r.name.lower() for r in self.rooms]:
                print "One or more rooms you tried to create already exist! " \
                    "Please try again."
                print spacer
                return
            if args["Office"]:
                new_room = Office(room)
                self.offices.append(new_room)
            elif args["Living"]:
                new_room = Living(room)
                self.livingspaces.append(new_room)
            self.rooms.append(new_room)
            new_rooms.append(new_room)
        print "You have successfully added the following rooom(s):"
        for new_room_ in new_rooms:
            print "Name: " + ''.join(new_room_.name) + " | Type: " \
                + new_room_.room_type
        print spacer

    def check_vacant_offices(self):
        """Add vacant offices to list; remove full ones from list"""
        for office in my_amity.offices:
            if len(office.occupants) < office.capacity:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
            elif len(office.occupants) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)

    def check_vacant_livingspaces(self):
        """Add vacant living spaces to list; remove full ones from list"""
        for livingspace in my_amity.livingspaces:
            if len(livingspace.occupants) < livingspace.capacity:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.capacity:
                if livingspace in self.vacant_livingspaces:
                    self.vacant_livingspaces.remove(livingspace)

    def add_person(self, args):
        """Add new person"""
        print spacer
        self.name = args["<first_name>"] + " " + args["<last_name>"]
        self.wants_space = "Yes" if args.get("<wants_space>") is "Y" else "No"
        if args["Staff"]:
            if self.wants_space == "Yes":
                if my_amity.offices:
                    my_amity.check_vacant_offices()
                    if not self.vacant_offices:
                        print "There are no vacant offices at this time."
                        print "Please try again later."
                        print spacer
                        return
                    office_choice = random.choice(self.vacant_offices)
                    self.new_person = Staff(self.name)
                    office_choice.occupants.append(self.new_person)
                    self.staff.append(self.new_person)
                    self.assigned_staff.append(self.new_person)
                    my_amity.success_added_person()
                    print "You have successfully allocated " + self.name + \
                        " of Employee ID " + str(self.new_person.emp_id) + \
                        "\nto the following office: " + office_choice.name
                    print spacer
                else:
                    print "There are no offices in the system."
                    print "Add an office using the create_room command " \
                        "and try again."
                    print spacer
                    return
            else:
                self.new_person = Staff(self.name)
                my_amity.success_added_person()
            self.staff.append(self.new_person)
        elif args["Fellow"]:
            if self.wants_space == "Yes":
                if my_amity.livingspaces:
                    my_amity.check_vacant_livingspaces()
                    if not self.vacant_livingspaces:
                        print "There are no vacant living spaces at this time."
                        print "Please try again later."
                        print spacer
                        return
                    living_choice = random.choice(self.vacant_livingspaces)
                    self.new_person = Fellow(self.name)
                    living_choice.occupants.append(self.new_person)
                    self.fellows.append(self.new_person)
                    self.assigned_fellows.append(self.new_person)
                    my_amity.success_added_person()
                    print "You have successfully allocated " + self.name + \
                        " of Employee ID " + str(self.new_person.emp_id) + \
                        "\nto the following living space: " + \
                        living_choice.name
                    print spacer
                else:
                    print "There are no living spaces in the system."
                    print "Add a living space using the create_room command " \
                        "and try again."
                    print spacer
                    return
            else:
                self.new_person = Fellow(self.name)
                my_amity.success_added_person()
            self.fellows.append(self.new_person)
        self.people.append(self.new_person)

    def success_added_person(self):
        """Success message when person has been successfully added"""
        print spacer
        print "You have successfully added the following person:"
        print "Name: " + self.name + " | Employee ID: " + \
            str(self.new_person.emp_id) + \
            "\nJob Type: " + self.new_person.job_type + \
            " | Wants Space?: " + self.wants_space
        print spacer

    def reallocate_person(self, args):
        """Reallocate person to another room"""

my_amity = Amity()
