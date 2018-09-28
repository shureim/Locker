import unittest
from user import User

class TestUser(unittest.TestCase) :

    """
    Test class that defines test cases for the user behaviour.

    Args :

    unittest.TestCase  TestCase class that helps in creating test cases.

    """
    def setUp(self) :
        """
        set up method  to run before each test cases
        """

        self.new_user("John", "Facebook", "john@gmail.com" "James001")

     def test__init__(self) :
        """
        test init  test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.userName, "John")
        self.assertEqual(self.new_user.accountName, "Facebook")
        self.assertEqual(self.new_user.email, "john@gmail.com")
        self.assertEqual(self.new_user.password, "James001")

if __name__ == "__main__" :
    unittest.main()        