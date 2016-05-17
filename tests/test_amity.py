import unittest
import os
from models.amity import Amity


class TestRooms(unittest.TestCase):

    def setUp(self):
        self.test_amity = Amity()

        """Create living space"""
        self.test_amity.create_room({
            "<room_name>": ["LivingA"],
            "Living": True,
            "Office": False
        })

        """Create office"""
        self.test_amity.create_room({
            "<room_name>": ["OfficeA"],
            "Living": False,
            "Office": True
        })

        # Assign rooms to variables
        self.livinga = self.test_amity.livingspaces[0]
        self.officea = self.test_amity.offices[0]

        """Add fellows"""
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow",
            "<wants_space>": "Y",
            "Fellow": True,
            "Staff": False
        })

        """Add staff member"""
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Staff",
            "<wants_space>": "Y",
            "Fellow": False,
            "Staff": True
        })
        # Assign people to variables
        self.testfellow = self.test_amity.people[0]
        self.teststaff = self.test_amity.people[1]

    def test_create_room(self):
        """Test creation of rooms"""
        # LivingA and OfficeA from setup() added to relevant lists
        self.assertEqual(2, len(self.test_amity.rooms))
        self.assertEqual(1, len(self.test_amity.livingspaces))
        self.assertEqual(1, len(self.test_amity.offices))

        """Test creation of multiple living spaces"""
        self.test_amity.create_room({
            "<room_name>": ["LivingB", "LivingC"],
            "Living": True,
            "Office": False
        })
        # Two living spaces added to list of rooms and list of living spaces
        self.assertEqual(4, len(self.test_amity.rooms))
        self.assertEqual(3, len(self.test_amity.livingspaces))

        """Test creation of multiple offices"""
        self.test_amity.create_room({
            "<room_name>": ["OfficeB", "OfficeC"],
            "Living": False,
            "Office": True
        })
        # Two offices added to list of rooms and list of offices
        self.assertEqual(6, len(self.test_amity.rooms))
        self.assertEqual(3, len(self.test_amity.offices))

        """Test that duplicate rooms are not added"""
        self.test_amity.create_room({
            "<room_name>": ["OfficeA", "OfficeB"],
            "Living": False,
            "Office": True
        })
        # Duplicate rooms not added to any list
        self.assertEqual(6, len(self.test_amity.rooms))
        self.assertEqual(3, len(self.test_amity.offices))
        # Error message displayed

    def test_add_person(self):
        """Test addition of people"""
        #  Test Fellow and Test Staff from setup() added to relevant lists
        self.assertEqual(2, len(self.test_amity.people))
        self.assertEqual(1, len(self.test_amity.fellows))
        self.assertEqual(1, len(self.test_amity.staff))

        """Test allocation of those who want space"""
        # Check that people have been appended to rooms' lists of occupants
        self.assertEqual(1, len(self.livinga.occupants))
        self.assertEqual(1, len(self.officea.occupants))

    def test_reallocate_person(self):
        """Add another living space"""
        self.test_amity.create_room({
            "<room_name>": ["LivingB"],
            "Living": True,
            "Office": False
        })

        # Assign LivingB to variable
        self.livingb = self.test_amity.livingspaces[1]

        """Reallocate Test Fellow from LivingA to LivingB"""
        self.test_amity.reallocate_person({
            "<employee_id>": int(self.testfellow.emp_id),
            "<new_room_name>": "LivingB"
        })

        # Fellow no longer in LivingA's list of occupants
        self.assertEqual(0, len(self.livinga.occupants))
        # Fellow now in LivingB's list of occupants
        self.assertEqual(1, len(self.livingb.occupants))

    def test_print_allocations(self):
        """
        Test that allocations are displayed on screen
        and printed to a text file if specified
        """
        self.test_amity.print_allocations({
            "--o": "myfile.txt"
        })
        # File is created
        self.assertTrue(os.path.exists("myfile.txt"))
