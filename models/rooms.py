class Room(object):
    """
    Creates a Room object. Classes Office and Living inherit from it
    """
    def __init__(self, name):
        self.occupants = []
        self.name = name

    def __repr__(self):
        return "<Room %s>" % self.name

    @property
    def room_type(self):
        return self.__class__.__name__


class Office(Room):
    capacity = 6

    def __init__(self, name):
        super(Office, self).__init__(name)

    def __repr__(self):
        return "<Office %s>" % self.name


class Living(Room):

    capacity = 4

    def __init__(self, name):
        super(Living, self).__init__(name)

    def __repr__(self):
        return "<Living space %s>" % self.name
