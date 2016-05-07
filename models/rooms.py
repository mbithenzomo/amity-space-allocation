class Room():
    '''
    Creates a Room object. Classes Office and Living inherit from it
    '''

    def create_room(self, args):
        ''' Creates new room(s) '''

        room_type = "Living Space" if args["Living"] else "Office" # set room type
        rooms = tuple((room, room_type) for room in args["<room_name>"]) # add rooms to tuple

        ''' Confirmation message '''
        print "You have successfully added the following rooom(s):" 
        for room in args["<room_name>"]:
            print "Name: " + ''.join(room) + " | Type: " + room_type

    def view_allocations(self, args):
        ''' Prints all room allocations '''
        pass
        # fetch allocations data from db. Table with columns: NAME | ROOM TYPE | FULLY OCCUPIED | VACANCIES AVAILABLE 


class Office(Room):

    capacity = 6

    def view_unallocated(self):
        ''' Prints all offices with vacancies ''' 
        pass
        # fetch unallocated offices from db

    def view_all_details(self):
        ''' Prints details of all offices '''
        pass
        # view details of all offices. NAME | FULLY OCCUPIED (T/F) | VACANCIES AVAILABLE

    def view_ind_details(self, office_id):
        ''' Prints details of an individual office '''
        pass
        # view details of individual office

    def allocate_office(self, staff_id, office_id):
        ''' Allocates a staff member to an office '''
        pass
        # add person to office

class Living(Room):

    capacity = 4

    def view_unallocated(self):
        ''' Prints all living spaces with vacancies ''' 
        pass
        # fetch unallocated offices from db

    def view_all_details(self):
        ''' Prints details of all living spaces '''
        pass
        # view details of all offices. NAME | FULLY OCCUPIED (T/F) | VACANCIES AVAILABLE

    def view_ind_details(self, lspace_id):
        ''' Prints details of an individual living space '''
        pass
        # view details of individual office

    def allocate_livingspace(self, fellow_id, lspace_id):
        ''' Allocates a person to an living space '''
        pass
        # add person to office