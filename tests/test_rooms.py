import unittest
from models.rooms import Room
from models.persons import Person

class TestRooms(unittest.TestCase):

    def set_office(self):
        ''' Create a new office '''
        self.office = Room("Oculus", "office")

    def set_livingspace(self):
        ''' Create a new living space '''
        self.livingspace = Room("Emerald", "livingspace")

    def test_office_capacity(self):
        ''' Check that capacity of office is 6 '''
        result = self.office.get_capacity()
        self.assertEqual(6, result)

    def test_livingspace_capacity(self):
        ''' Check that capacity of living space is 4 '''
        result = self.livingspace.get_capacity()
        self.assertEqual(4, result)

    def test_assign_occupant(self):
        ''' Check that assign_occupant function adds occupant to living space '''
        self.occupant = Person("Mbithe", "fellow")
        self.livingspace.assign_occupant(self.occupant)
        self.assertTrue(self.livingspace.is_occupied())