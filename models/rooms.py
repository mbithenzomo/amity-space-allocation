class Room(object):
    """
    Creates a Room object. Classes Office and Living inherit from it
    """

    def __init__(self, name=''):
        self.occupants = []  # list of occupants in room
        self.name = name

    def view_allocations(self, args):
        """ Prints all room allocations """
        pass

    def __repr__(self):
        return '<Room %s>' % self.name

    @property
    def room_type(self):
        return self.__class__.__name__


class Office(Room):
    capacity = 6  # set capacity

    def __init__(self, name):
        super(Office, self).__init__(name)

    def view_all_details(self):
        """ Prints details of all offices """
        pass
        # view details of all offices. NAME | FULLY OCCUPIED (T/F) | VACANCIES AVAILABLE

    def view_ind_details(self, office_id):
        """ Prints details of an individual office """
        pass
        # view details of individual office

    def allocate_office(self, staff_id, office_id):
        """ Allocates a staff member to an office """
        pass
        # add person to office

    def __repr__(self):
        return '<Office %s>' % self.name


class Living(Room):

    capacity = 4  # set capacity

    def __init__(self, name):
        super(Living, self).__init__(name)

    def view_unallocated(self):
        """ Prints all offices with free spaces """

        # spaces = capacity - len(occupants) # get number of spaces available
        #
        # print "The following living spaces have free spaces: "
        # for livingspace in livingspaces:
        #     if spaces != 0:
        #         print  "Name: " + ''.join(room) + " | Spaces available: " + spaces

    def view_all_details(self):
        """ Prints details of all living spaces """
        pass
        # view details of all offices. NAME | FULLY OCCUPIED (T/F) | VACANCIES AVAILABLE

    def view_ind_details(self, lspace_id):
        """ Prints details of an individual living space """
        pass
        # view details of individual office

    def allocate_livingspace(self, fellow_id, lspace_id):
        """ Allocates a person to an living space """
        pass
        # add person to office
