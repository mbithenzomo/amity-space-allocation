class Room(object):
    """
    Creates a Room object. 
    Classes Office and LivingSpace inherit from it.
    """

    def __init__(self, name):
        """
        Initializing the class with a name
        """
        self.name = name

class Office(Room):
    """
    Creates an Office object.
    """

    def __init__(self):
        self.capacity = 6 # set capacity of office space
        self.occupants = [] # create list of occupants

    def is_occupied():
        self.is_occupied = False # default value of is_occupied is False
        return self.is_occupied

    def get_occupants():
        return self.occupants # return list of occupants

    def assign_occupant(occupant):
        if  self.occupants < self.capacity:
            self.occupants.append() # assign parameter as new occupant
            self.is_occupied = True # sets is_occupied to True
        else:
            print "Sorry, this office has reached its maximum capacity."

class LivingSpace(Room):
    """
    Creates a LivingSpace object.
    """

    def __init__(self):
        self.capacity = 4 # set capacity of living space
        self.occupants = [] # create list of occupants

    def is_assigned():
        self.is_occupied = False # default value of is_occupied is False
        return self.is_occupied

    def get_occupants():
        return self.occupants # return list of occupants

    def assign_occupant(occupant):
        if  self.occupants < self.capacity:
            self.occupants.append() # assign parameter as new occupant
            self.is_occupied = True # sets is_occupied to True
        else:
            print "Sorry, this living space has reached its maximum capacity."