import unittest
from password import Details


class TestDetails(unittest.TestCase):

    """
    Test class that defines test for the details class behaviours

    """

    def setUp(self):
        self.create_details = Details("Karushi", "Karushi1")

    def tearDown(self):
        Details.create_details = []

    def test_init_(self):
        self.assertEqual(self.create_details.account_name, "Karushi")
        self.assertEqual(self.create_details.account_password, "Karushi1")

    def test_save_details(self)
    """
    test_save_details test case to test if the details object is saved

    """
    self.new_details.save_details  

if __name__ == '__main__':
    unittest.main()
