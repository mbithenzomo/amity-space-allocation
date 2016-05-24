import unittest
import os
from models.amity import Amity


class TestAmity(unittest.TestCase):

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

        """Add fellow that wants space"""
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow",
            "<wants_space>": "Y",
            "Fellow": True,
            "Staff": False
        })

        """Add staff member that wants space"""
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

    def test_add_person(self):
        """Test addition of people"""
        #  Test Fellow and Test Staff from setup() added to relevant lists
        self.assertEqual(2, len(self.test_amity.people))
        self.assertEqual(1, len(self.test_amity.fellows))
        self.assertEqual(1, len(self.test_amity.staff))

        """Test allocation of those who want space"""
        # Check that people have been appended to rooms' lists of occupants
        self.assertEqual(2, len(self.officea.occupants))

    def test_vacant_offices(self):
        """Test that vacant rooms are added to relevant list"""
        # Add office
        self.test_amity.create_room({
            "<room_name>": ["OfficeB"],
            "Living": False,
            "Office": True
        })

        self.test_amity.check_vacant_rooms()

        # Check if OfficeB has been appended to relevant lists
        self.assertEqual(2, len(self.test_amity.vacant_offices))
        self.assertEqual(3, len(self.test_amity.vacant_rooms))

    def test_reallocate_person(self):
        """Add another office"""
        self.test_amity.create_room({
            "<room_name>": ["OfficeB"],
            "Living": False,
            "Office": True
        })
        # Assign OfficeB to variable
        officeb = self.test_amity.offices[1]

        """Test reallocation of Test Staff from OfficeA to OfficeB"""
        self.test_amity.reallocate_person({
            "<employee_id>": int(self.teststaff.emp_id),
            "<new_room_name>": "OfficeB"
        })
        # Staff member no longer in OfficeA's list of occupants
        self.assertEqual(1, len(self.officea.occupants))
        # Staff member now in OfficeB's list of occupants
        self.assertEqual(1, len(officeb.occupants))

        """Add another living space"""
        self.test_amity.create_room({
            "<room_name>": ["LivingB"],
            "Living": True,
            "Office": False
        })
        # Assign LivingB to variable
        livingb = self.test_amity.livingspaces[1]

        """Test allocation of Test Fellow to LivingB"""
        self.test_amity.reallocate_person({
            "<employee_id>": int(self.testfellow.emp_id),
            "<new_room_name>": "LivingB"
        })
        # Fellow now in LivingB's list of occupants
        self.assertEqual(1, len(livingb.occupants))

        """Test that staff cannot be allocated to living space"""
        self.test_amity.reallocate_person({
            "<employee_id>": int(self.teststaff.emp_id),
            "<new_room_name>": "LivingB"
        })
        # Staff not added to LivingB's list of occupants
        self.assertEqual(1, len(livingb.occupants))

    def test_load_people(self):
        """
        Test that people can be added to the app from a
        user-defined text file
        """

        """Add office to have more vacant offices for people from text file """
        self.test_amity.create_room({
            "<room_name>": ["OfficeC"],
            "Living": False,
            "Office": True
        })

        self.test_amity.load_people({"<filename>": "people.txt"})
        # People from file are added to application
        self.assertEqual(12, len(self.test_amity.people))
        self.assertEqual(7, len(self.test_amity.fellows))
        self.assertEqual(5, len(self.test_amity.staff))

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
        # Data is entered
        with open("myfile.txt") as myfile:
            lines = myfile.readlines()
            self.assertTrue("LivingA\n" in lines)
            self.assertTrue("OfficeA\n" in lines)
            self.assertTrue("Test Fellow, Test Staff\n" in lines)
        os.remove("myfile.txt")

    def test_print_unallocated(self):
        """
        Test that unallocated people are displayed on screen
        and printed to a text file if specified
        """
        # Add fellow that does not want space
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow2",
            "<wants_space>": "N",
            "Fellow": True,
            "Staff": False
        })
        self.test_amity.print_unallocated({
            "--o": "myfile2.txt"
        })
        # File is created
        self.assertTrue(os.path.exists("myfile2.txt"))
        # Data is entered
        with open("myfile2.txt") as myfile:
            lines = myfile.readlines()
            self.assertTrue("Unallocated People\n" in lines)
            self.assertTrue("Test Fellow2\n" in lines)
        os.remove("myfile2.txt")
