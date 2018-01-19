import unittest
from password import Password


class testpassword(unttest.testpassword):

    def setUp(self):
        self.create_account = Password("karushi", "noelkarush")

    def tearDown(self):
        password.create_account = []

    def test_init(self):
        
