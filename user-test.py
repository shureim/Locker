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
        self.new_user = User("John", "John",  "John001") #new user
    def tearDown(self) :
        """
        tear down method does clean up after each test case has run
        """
        User.user_list = []
    def test__init__(self) :
        """
        test init  test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.firstName, "John")
        self.assertEqual(self.new_user.lastName, "John")
        self.assertEqual(self.new_user.user_password, "John001")
    def test_save_user(self) :
        """
        test save user test case to test if ths user is saved into the user list.
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
    def test_save_multiple_user(self) :
        """
        test save multiple user   test case to check if we can save multiple user.
        """
        self.new_user.save_user()
        test_user = User("Tarick", "Tarick",  "Tarick002") #new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    def test_delete_user(self) :
        """
        test delete user -test case to delete already saved user from the user list
        """
        self.new_user.save_user()
        test_user = User("peter", "Peter",  "Peter003") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)





    def test_find_user_by_lastName(self):
        """
        test find user by accountName-test case to find user  by accountname and diplay the information
        """
        self.new_user.save_user()
        test_user = User("Joe", "Joe", "Joe004") # new user
        test_user.save_user()
        found_user = User.find_by_lastName("Joe")
        self.assertEqual(found_user.user_password,test_user.user_password)

    def test_user_exists(self) :
        """
        test user exists -test case to test if the user exists and if not return Boolean
        """
        self.new_user.save_user()
        test_user = User("marcus", "marcus","Marcus005") # new user
        test_user.save_user()
        user_exists = User.user_exist("marcus")
        self.assertTrue(user_exists)

    def test_display_all_user(self) :
        """
        test display all user -test case to return the user list that is saved
        """
        self.assertEqual(User.display_user(), User.user_list)



if __name__ == "__main__" :
    unittest.main()        