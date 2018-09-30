import unittest
from credential import Credential

class TestCredential(unittest.TestCase) :
    """
    Test class that defines test cases for the credential behaviour.
    Args :
    unittest.TestCase  TestCase class that helps in creating test cases.
    """
    def SetUp(self) :
        """
        setup -method to run before each test case 
        """
        self.new_credential = Credential("snapchat", "chat@gmail.com", "Chat001") # new credential

    def tearDown(self) :
        """
        tear down method does clean up after each test case has run
        """
        Credential.credential_list = [] 
    def test__init__(self) :
        """
        test init  test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.accountName, "snapchat")
        self.assertEqual(self.new_credential.email, "chat@gmail.com")
        self.assertEqual(self.new_credential.password, "chat001")
    # def test_save_credential(self) :
    #     """
    #     test save credential test case to test if ths credential is saved into the credential list.
    #     """
    #     self.new_credential.save_credential()
    #     self.assertEqual(len(Credential.credential_list),1)
    # def test_save_multiple_credential(self) :
    #     """
    #     test save multiple credential test case to check if we can save multiple credential.
    #     """
    #     self.new_credential.save_credential()
    #     test_credential = Credential("Instagram", "insta@gmail.com",  "Insta002") #new credential
    #     test_credential.save_credential()
    #     self.assertEqual(len(Credential.credential_list),2)

    # def test_delete_user(self) :

    #     """
    #     test delete user -test case to delete already saved user from the user list
    #     """
    #     self.new_credential.save_credential()
    #     test_credential = Credential("peter", "Peter",  "Peter003") # new user
    #     test_credential.save_credential()
    #     self.assertEqual(len(Credential.credential_list),2)


if __name__ == "__main__":
    unittest.main()


