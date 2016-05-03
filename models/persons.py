class Person(object):
    """
    Creates a Person object. 
    Classes Fellow and Staff inherit from it.
    """

    def __init__(self, fname, lname):
        """
        Initializing the class with a name
        """
        self.fname = fname
        self.lname = lname

class Fellow(Person):
    """
    Creates a Fellow object.
    """

    def __init__(self):
        self.type = "Fellow" # set type to be Fellow


class Staff(Person):
    """
    Creates a Staff object.
    """

    def __init__(self):
        self.type = "Staff" # set type to be Staff
