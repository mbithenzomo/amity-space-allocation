import unittest
import os
from db.database import Database
from models.amity import Amity


class TestDatabase(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("test.db")
        except:
            pass

    def load_data_into_amity(self, amity):
        # Add data to application
        amity.create_room({
            "<room_name>": ["LivingA"],
            "Living": True,
            "Office": False
        })
        amity.create_room({
            "<room_name>": ["OfficeA"],
            "Living": False,
            "Office": True
        })
        amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow",
            "<wants_space>": "Y",
            "Fellow": True,
            "Staff": False
        })
        amity.add_person({
            "<first_name>": "Test",
            "<last_name>": "Staff",
            "<wants_space>": "Y",
            "Fellow": False,
            "Staff": True
        })

        return amity

    def test_save_state(self):
        """Test that application data can be saved to user-defined database"""
        amity = self.load_data_into_amity(Amity())
        test_db = Database(amity)
        test_db.save_state({
            "--db": "test.db"
        })

        # File is created
        self.assertTrue(os.path.exists("test.db"))
        os.remove("test.db")

    def test_load_state(self):
        """
        Test that  data can be loaded to the application
        from an existing database
        """
        amity = self.load_data_into_amity(Amity())
        test_db = Database(amity)
        test_db.save_state({
            "--db": "test.db"
        })

        amity2 = Amity()
        test_db2 = Database(amity2)

        # Load data from previously created database
        test_db2.load_state({
            "<sqlite_database>": "test.db"
        })

        # Data is entered into the application
        print('in test_load_state', amity.people)
        print('in test_load_state', amity.rooms)
        print(len(amity.rooms))
        print(amity.livingspaces)
        self.assertEqual(2, len(amity.rooms))
        self.assertEqual(1, len(amity.livingspaces))
        self.assertEqual(1, len(amity.offices))
        self.assertEqual(2, len(amity.people))
        self.assertEqual(1, len(amity.fellows))
        self.assertEqual(1, len(amity.staff))

        os.remove("test.db")
