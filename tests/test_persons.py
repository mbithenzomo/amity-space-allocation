import unittest
from models.persons import Person

class TestPersons(unittest.TestCase):

    def test_add_person(self):
        ''' Check that people can be added with different kinds of input '''
        
        ''' Check adding fellow with all parameters '''
        person1 = Person("Mbithe", "Nzomo", "Fellow", "Y")
        result1 = person1.get_person_details()
        self.assertEqual(("Mbithe", "Nzomo", "Fellow", "Y"), result1)
        
        ''' Check adding fellow without wants_space parameter '''
        person2 = Person("Margaret", "Ochieng", "Fellow")
        result2 = person2.get_person_details()
        self.assertEqual(("Margaret", "Ochieng", "Fellow", "N"), result2)
        
        ''' Check adding staff '''
        person3 = Person("Jackson", "Saya", "Staff")
        result3 = person3.get_person_details()
        self.assertEqual(("Jackson", "Saya", "Staff", "N"), result3)

    def test_job_type(self):
        
        ''' Check fellow job type '''
        fellow = Person("Mbithe", "Nzomo", "Fellow", "Y")
        result =  fellow.get_job_type()
        self.assertEqual("Fellow", result)

        ''' Check staff job type '''
        staff = Person("Jackson", "Saya", "Staff")
        result =  staff.get_job_type()
        self.assertEqual("Staff", result)