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

    def test_save_details(self):
        """
        test_save_details test case to test if the details object is saved
        """
        self.create_details.save_details()
        self.assertEqual(len(Details.create_details), 1)

    def test_save_multiple_details(self):
        '''
        test_save_details_multiple_details to check if we can save save multiple details

        '''
        self.create_details.save_details()
        test_details = Details("Karushi", "Karushi1")
        test_details.save_details()
        self.assertEqual(len(Details.create_details), 2)

    def test_delete_details(self):
        '''
        test_delete_details to test if we can remove a details
        '''
        self.create_details.save_details()
        test_details = Details("Karushi", "Karushi1")
        test_details.save_details()

        self.create_details.delete_details()
        self.assertEqual(len(Details.create_details), 1)

    def test_find_details_by_name(self):
        '''
        test to check if we can find a details by name and display information
        '''
        self.create_details.save_details()
        test_details = Details("Karushi", "Karushi1")
        test_details.save_details()

        found_details = Details.test_find_details_by_name()

        self.assertEqual(found_details.account_password)


if __name__ == '__main__':
    unittest.main()
