import unittest
from models.rooms import Room

class TestRooms(unittest.TestCase):

    def test_office_capacity(self):

        ''' For office '''
        office = Room("Oculus", "Office")
        result = office.get_capacity()
        self.assertEqual(6, result)

        ''' For livingspace '''
        livingspace = Room("Emerald", "Livingspace")
        result = livingspace.get_capacity()
        self.assertEqual(4, result)

    def test_room_type(self):

        ''' For office '''
        office = Room("Oculus", "Office")
        result = office.get_room_type()
        self.assertEqual("Office", result)

        ''' For livingspace '''
        livingspace = Room("Emerald", "Livingspace")
        result = livingspace.get_room_type()
        self.assertEqual("Livingspace", result)
        
        