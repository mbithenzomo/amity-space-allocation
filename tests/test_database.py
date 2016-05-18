import unittest
import os
from db.database import Database
from models.amity import Amity


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.test_db = Database()
        self.test_amity = Amity()

        # Add data to application
        self.test_amity.create_room({
            "<room_name>": ["LivingA"],
            "Living": True,
            "Office": False
        })
        self.test_amity.create_room({
            "<room_name>": ["OfficeA"],
            "Living": False,
            "Office": True
        })
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow",
            "<wants_space>": "Y",
            "Fellow": True,
            "Staff": False
        })
        self.test_amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Staff",
            "<wants_space>": "Y",
            "Fellow": False,
            "Staff": True
        })

    def test_save_state(self):
        """Test that application data can be saved to user-defined database"""
        self.test_db.save_state({
            "--db": "test.db"
        })

        # File is created
        self.assertTrue(os.path.exists("test.db"))

        print self.test_amity.people


    def test_load_state(self):
        """
        Test that  data can be loaded to the application
        from an existing database
        """
        # Load data from previously created database
        self.test_db.load_state({
            "<sqlite_database>": "test.db"
        })

        # Data is entered into the application
        self.assertEqual(2, len(self.test_amity.rooms))
        self.assertEqual(1, len(self.test_amity.livingspaces))
        self.assertEqual(1, len(self.test_amity.offices))
        self.assertEqual(2, len(self.test_amity.people))
        self.assertEqual(1, len(self.test_amity.fellows))
        self.assertEqual(1, len(self.test_amity.staff))
