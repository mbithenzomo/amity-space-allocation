class Person(object):
    '''
    Creates a Person object. Classes Fellow and Staff inherit from it.
    '''

    def add_person(self, args):
        ''' Adds new person '''

        name = args["<first_name>"] + " " + args["<last_name>"]
        job_type = "Staff" if args["Staff"] else "Fellow" # set job type
        wants_space = "Yes" if args["<wants_space>"] is "Y" else "No" # set wants_space
        persons = tuple((name, job_type) for name in args["<first_name>"]) # add person to tuple

        ''' Confirmation message '''
        print "You have successfully added the following person:"
        print "Name: " + name + " | Job Type: " + job_type + " | Wants Space?:"  + " " + wants_space

class Staff(Person):

    job_type = "Staff"

    # def allocate_staff(self, staff_id):
    #     if self.wants_space == "Y":
    #         pass
    #         # randomly allocate a room

    # def reallocate(self, staff_id):
    #     # reallocate room

class Fellow(Person):

    job_type = "Fellow"

    # def allocate_fellow(self, fellow_id):
    #     if self.wants_space = "Y":
    #         # randomly allocate a room

    # def reallocate(self, fellow_id):
    #     # reallocate room



