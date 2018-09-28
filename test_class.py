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

        self.new_user = User("John", "Facebook", "john@gmail.com", "James001")

    # def tearDown(self) :
    #     User.user_list = []

    def test__init__(self) :
        """
        test init  test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.userName, "John")
        self.assertEqual(self.new_user.accountName, "Facebook")
        self.assertEqual(self.new_user.email, "john@gmail.com")
        self.assertEqual(self.new_user.password, "James001")

    def test_save_user(self) :
        """
        test save user test case to test if ths user is saved into the user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    # def test_save_multiple_user(self) :
    #     """
    #     test save multiple user   test case to check if we can save multiple user.
    #     """
    #     self.new_user.save_user()
    #     test.user = User("Tarick", "Instagram", "tarick@gmail.com", "Tarick002")
    #     test_user.save_user()
    #     self.assertEqual(len(User.user_list),2)





if __name__ == "__main__" :
    unittest.main()        