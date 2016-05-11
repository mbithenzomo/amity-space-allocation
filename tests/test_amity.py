import unittest
from models.rooms import Room
from models.amity import Amity

class TestRooms(unittest.TestCase):

    def setUp(self):
        pass

    def test_create_rooms(self):
        test_amity = Amity()
        test_amity.create_room({"<room_name>": ["Emerald", "Jade"], "Living": True, "Office": False})
        self.assertEqual(2, len(test_amity.rooms))
        self.assertEqual(2, len(test_amity.livingspaces))
        test_amity.create_room({"<room_name>": ["Valhalla", "Oculus"], "Living": False, "Office": True})
        self.assertEqual(4, len(test_amity.rooms))
        self.assertEqual(2, len(test_amity.offices))
