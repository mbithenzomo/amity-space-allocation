class Person(object):
    """
    Creates a Person object. Classes Fellow and Staff inherit from it.
    """
    def __init__(self, name):
        self.name = name
        self.emp_id = id(self)


class Staff(Person):

    job_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)


class Fellow(Person):

    job_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)
