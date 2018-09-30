
class User :
    """
    class that generate new instance 

    """ 
    user_list = [] # empty user list
    def __init__(self, firstName, lastName, user_password ) :

        """
        __init__ method that help us create properties of the object

            Args :
            firstName :new user firstName .
            lastName : new user lastName .
            user_password : new user_password .
        """
    #     self.firstName = firstName
    #     self.lastName = lastName
    #     self.user_password = user_password
        
    # def save_user(self) :
    #     """
    #     save_user method saves user object into users list.
    #     """
    #     User.user_list.append(self)

    # def delete_user(self) :
    #     """
    #     delete user method removes unwanted user object from users list
    #     """
    #     User.user_list.remove(self)
    # @classmethod #decorator
    # def find_by_lastName(cls, lastName) :
    #     """
    #     find by accountName method  that takes in the accountname and returns the user tha matches that user password.
        
    #     Args:
    #         accountName to search for
    #     Returns :
    #         user of the person that matches tha password
    #     """
    #     for user in cls.user_list :
    #         if user.lastName == lastName :
    #             return user

    # @classmethod # decorator
    # def user_exist (cls, lastName) :
    #     """
    #     user exist method that checks if the user exist

    #     Args :
    #         search if the username exist
        
    #     Return :
    #         if the user does not exist the return with boolean
    #     """
    #     for user in cls.user_list:
    #         if user.lastName == lastName:
    #             return True
    #     return False

    # @classmethod # decorator
    # def display_user(cls) :
    #     """
    #     method that returns users list
    #     """

    #     return cls.user_list
    



