import random
from rooms import Office, Living
from people import Staff, Fellow, StaffFromDatabase, FellowFromDatabase
from termcolor import colored

spacer = " "
border = colored("*" * 5, 'cyan').center(80)


class Amity(object):
    def __init__(self):
        self.rooms = []
        self.vacant_rooms = []
        self.offices = []
        self.vacant_offices = []
        self.livingspaces = []
        self.vacant_livingspaces = []
        self.people = []
        self.allocated_people = []
        self.unallocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []

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
                self.check_vacant_offices()
            elif args["Living"]:
                new_room = Living(room)
                self.livingspaces.append(new_room)
                self.check_vacant_livingspaces()
            self.rooms.append(new_room)
            new_rooms.append(new_room)
        print "You have successfully added the following rooom(s):"
        for new_room_ in new_rooms:
            print "Name: " + ''.join(new_room_.name) + " | Type: " \
                + new_room_.room_type
        print spacer

    def check_vacant_offices(self):
        """Add vacant offices to lists; remove full ones from lists"""
        for office in self.offices:
            if len(office.occupants) < office.capacity:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            elif len(office.occupants) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)

    def check_vacant_livingspaces(self):
        """Add vacant living spaces to lists; remove full ones from lists"""
        for livingspace in self.livingspaces:
            if len(livingspace.occupants) < livingspace.capacity:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.capacity:
                if livingspace in self.vacant_livingspaces:
                    self.vacant_livingspaces.remove(livingspace)
                    self.vacant_rooms.remove(livingspace)

    def add_person(self, args):
        """Add new person"""
        print spacer
        name = args["<first_name>"] + " " + args["<last_name>"]
        wants_space = "Yes" if args.get("<wants_space>") is "Y" else "No"
        if args["Staff"]:
            if wants_space == "Yes":
                if self.offices:
                    self.check_vacant_offices()
                    if not self.vacant_offices:
                        print "There are no vacant offices at this time."
                        print "Please try again later."
                        print spacer
                        return
                    office_choice = random.choice(self.vacant_offices)
                    new_person = Staff(name)
                    office_choice.occupants.append(new_person)
                    self.staff.append(new_person)
                    self.allocated_staff.append(new_person)
                    self.allocated_people.append(new_person)
                    self.success_added_person(new_person, wants_space)
                    print "You have successfully allocated " + name + \
                        " of Employee ID " + str(new_person.emp_id) + \
                        "\nthe following office: " + office_choice.name
                    print spacer
                else:
                    print "There are no offices in the system."
                    print "Add an office using the create_room command " \
                        "and try again."
                    print spacer
                    return
            else:
                new_person = Staff(name)
                self.success_added_person(new_person, wants_space)
                self.staff.append(new_person)
        elif args["Fellow"]:
            if wants_space == "Yes":
                if self.livingspaces:
                    self.check_vacant_livingspaces()
                    if not self.vacant_livingspaces:
                        print "There are no vacant living spaces at this time."
                        print "Please try again later."
                        print spacer
                        return
                    living_choice = random.choice(self.vacant_livingspaces)
                    new_person = Fellow(name)
                    living_choice.occupants.append(new_person)
                    self.fellows.append(new_person)
                    self.allocated_fellows.append(new_person)
                    self.allocated_people.append(new_person)
                    self.success_added_person(new_person, wants_space)
                    print "You have successfully allocated " + name + \
                        " of Employee ID " + str(new_person.emp_id) + \
                        "\nthe following living space: " + \
                        living_choice.name
                    print spacer
                else:
                    print "There are no living spaces in the system."
                    print "Add a living space using the create_room command " \
                        "and try again."
                    print spacer
                    return
            else:
                new_person = Fellow(name)
                self.success_added_person(new_person, wants_space)
                self.fellows.append(new_person)
        self.people.append(new_person)

    def add_person_from_db(self, args):
        """Add new person from an existing database"""
        print spacer
        is_fellow = args["is_fellow"]
        first_name = args["first_name"]
        last_name = args["last_name"]
        emp_id = args["emp_id"]
        wants_space = "No"
        if is_fellow:
            new_person = FellowFromDatabase(
                is_fellow, first_name, last_name, emp_id
            )
            self.fellows.append(new_person)
        else:
            new_person = StaffFromDatabase(
                is_fellow, first_name, last_name, emp_id
            )
            self.staff.append(new_person)
        self.success_added_person(new_person, wants_space)
        self.people.append(new_person)

    def success_added_person(self, new_person, wants_space):
        """Success message when person has been successfully added"""
        print "You have successfully added the following person:"
        print "Name: " + new_person.name + " | Employee ID: " + \
            str(new_person.emp_id) + \
            "\nJob Type: " + new_person.job_type + \
            " | Wants Space?: " + wants_space
        print spacer

    def reallocate_person(self, args):
        """(Re)allocate person to (another) room"""
        print spacer
        emp_id = int(args["<employee_id>"])
        new_person = None
        """Check that employee ID entered exists"""
        for p in self.people:
            if p.emp_id == emp_id:
                new_person = p
        if new_person is None:
            print "The employee ID you have entered does not exist."
            print "Please try again."
            print spacer
            return

        new_room_name = args["<new_room_name>"]
        for r in self.rooms:
            if r.name == new_room_name:
                new_room = r

        """Check that room entered exists"""
        if new_room_name not in [r.name for r in self.rooms]:
            print "The room you have entered does not exist."
            print "Please try again."
            print spacer
            return

        """Check that room entered is vacant"""
        if new_room_name not in [r.name for r in self.vacant_rooms]:
            print "The room you entered, " + new_room_name + \
                ", is not vacant at this time."
            print "Please try again later."
            print spacer
            return

        if new_person.job_type == "Staff":
            """Prevent staff from being allocated living spaces"""
            if new_room.room_type == "Living":
                print "Staff members cannot be allocated " \
                    "living spaces."
                print spacer
                return
            else:
                """
                Check if staff member has already been allocated an office
                """
                for office in self.vacant_offices:
                    if new_person.emp_id in \
                            [person.emp_id for person in office.occupants]:
                        if new_room == office:
                            """
                            Prevent staff member from being allocated \
                            the same office
                            """
                            print new_person.name + " is already an occupant" \
                                " of the office " + new_room.name + "."
                            print spacer
                            return
                        else:
                            """Remove staff member from current office"""
                            office.occupants.remove(new_person)
                """Add staff member to new office"""
                new_room.occupants.append(new_person)
                self.allocated_staff.append(new_person)
                self.allocated_people.append(new_person)
                print "You have successfully allocated " + new_person.name + \
                    " of Employee ID " + str(new_person.emp_id) + \
                    "\nthe following office: " + new_room.name

        elif new_person.job_type == "Fellow":
            if new_room.room_type == "Office":
                """
                Check if fellow has already been allocated an office
                """
                for office in self.vacant_offices:
                    if new_person.emp_id in \
                            [person.emp_id for person in office.occupants]:
                        if new_room == office:
                            """
                            Prevent fellow from being allocated \
                            the same office
                            """
                            print new_person.name + " is already an occupant" \
                                " of the office " + new_room.name + "."
                            print spacer
                            return
                        else:
                            """Remove fellow from current office"""
                            office.occupants.remove(new_person)
                """Add fellow to new office"""
                new_room.occupants.append(new_person)
                self.allocated_fellows.append(new_person)
                self.allocated_people.append(new_person)
                print "You have successfully allocated " + new_person.name + \
                    " of Employee ID " + str(new_person.emp_id) + \
                    "\nthe following office: " + new_room.name
            elif new_room.room_type == "Living":
                """
                Check if fellow has already been allocated a living space
                """
                for livingspace in self.vacant_livingspaces:
                    if new_person.emp_id in \
                            [person.emp_id for person
                                in livingspace.occupants]:
                        if new_room == livingspace:
                            """
                            Prevent fellow from being allocated \
                            the same living space
                            """
                            print new_person.name + " is already an occupant" \
                                " of the living space " + new_room.name + "."
                            print spacer
                            return
                        else:
                            """Remove fellow from current living space"""
                            livingspace.occupants.remove(new_person)
                """Add fellow to new living space"""
                new_room.occupants.append(new_person)
                self.allocated_fellows.append(new_person)
                self.allocated_people.append(new_person)
                print "You have successfully allocated " + new_person.name + \
                    " of Employee ID " + str(new_person.emp_id) + \
                    "\nthe following living space: " + new_room.name
        if new_person in self.unallocated_people:
            self.unallocated_people.remove(new_person)
        print spacer

    def load_people(self, args):
        """Add people to rooms from a txt file"""
        filename = args["<filename>"]
        with open(filename, 'r') as my_file:
            people = my_file.readlines()
            for p in people:
                p = p.split()
                if p:
                    first_name = p[0]
                    last_name = p[1]
                    if p[2] == "FELLOW":
                        is_staff = False
                        is_fellow = True
                    else:
                        is_staff = True
                        is_fellow = False
                    if len(p) == 4:
                        wants_space = p[3]
                    else:
                        wants_space = None

                    self.add_person({
                            "<first_name>": first_name.title(),
                            "<last_name>": last_name.title(),
                            "<wants_space>": wants_space,
                            "Fellow": is_fellow,
                            "Staff": is_staff
                        })

    def print_allocations(self, args):
        """Print list of occupants per room to the  \
        screen and optionally to a text file"""
        print spacer
        output = ""
        for r in self.rooms:
            output += r.name + "\n"
            output += "-" * 50 + "\n"
            if r.occupants:
                output += ", ".join(p.name for p in r.occupants) + "\n"
                output += spacer + "\n"
            else:
                output += "This room has no occupants.\n"
                output += spacer + "\n"
        if not self.rooms:
            output += "There are no rooms in the system.\n"
            output += "Add a room using the create_room command" \
                " and try again.\n"
        print output
        if args["--o"]:
            with open(args["--o"], 'wt') as f:
                f.write(output)
                print "The list of allocations has been saved " \
                    "to the following file: "
                print args["--o"]
                print spacer

    def print_unallocated(self, args):
        """Print list of unallocated people to the \
        screen and optionally to a text file"""
        print spacer
        output = ""
        output += "Unallocated People\n"
        output += "-" * 50 + "\n"
        for p in self.people:
            if p not in self.allocated_people:
                output += p.name + "\n"
                if p not in self.unallocated_people:
                    self.unallocated_people.append(p)
        if not self.people:
            output += "There are no people in the system.\n"
            output += "Add a person using the add_person command" \
                " and try again.\n"
        elif not self.unallocated_people:
            output += "There are no unallocated people in the system.\n"
        print output
        if args["--o"]:
            with open(args["--o"], 'wt') as f:
                f.write(output)
                print "The list of unallocated people has been saved " \
                    "to the following file: "
                print args["--o"]
                print spacer

    def print_room(self, args):
        """Print the names of all the people in room_name on the screen"""
        print spacer
        room_name = args["<room_name>"]
        if room_name not in [r.name for r in self.rooms]:
            print "The room you have entered does not exist."
            print "Please try again."
            print spacer
            return
        for r in self.rooms:
            if r.name == room_name:
                room = r
                print room.name
                print "-" * 50
                if room.occupants:
                    for p in room.occupants:
                        print p.name
                else:
                    print "This room has no occupants."
                print spacer
