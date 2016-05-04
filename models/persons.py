class Person(object):
    """
    Creates a Person object.
    """

    def __init__(self, fname, lname, job_type, wants_space="N"):
        """
        Initializing the class with a name
        """
        self.fname = fname
        self.lname = lname
        self.job_type = job_type
        self.wants_space = wants_space

    def get_person_details(self):
        self.details = self.fname, self.lname, self.job_type, self.wants_space
        return self.details

    def get_job_type(self):
        return self.job_type
        
    def is_assigned():
        self.is_assigned = False # default value of is_assigned is False
        return self.is_assigned