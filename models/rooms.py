class Room(object):
    """
    Creates a Room object.
    """

    def __init__(self, name, room_type):
        """
        Initializing the class with a name and type
        """
        self.name = name
        self.room_type = room_type
        self.occupants = [] # create list of occupants
        if self.room_type == "Office":
            self.capacity = 6 # set office capacity to 6
        elif self.room_type == "Livingspace":
            self.capacity = 4 # set livingspace capacity to 4
        else:
            print "Please select a valid room type. Your options are: 'Office' and 'Livingspace'."

    def get_room_type(self):
        return self.room_type    

    def get_capacity(self):
        return self.capacity

    def is_occupied(self):
        self.is_occupied = False # default value of is_occupied is False
        return self.is_occupied

    def get_occupants(self):
        return self.occupants # return list of occupants

    def assign_occupant(occupant):
        # if  self.occupants < self.capacity:
        #     self.occupants.append(occupant) # assign parametecr as new occupant
        # else:
        #     print "Sorry, this room has reached its maximum capacity."
        pass

    def set_occupied(self):
        if len(self.occupants) > 0:
            self.is_occupied = True # sets is_occupied to True if list of occupants is not empty