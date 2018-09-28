class User :
    """
    class tha generate new instance 

    """ 
    user_list = [] # empty user list
    def __init__(self, userName, accountName, email, password) :

        """
        __init__ method that help us create properties of the object

            Args :
            username :new user username .
            accountName : new user accountName.
            email : new user email.
            password : new user  password.

        """
        self.userName = userName
        self.accountName = accountName
        self.email = email
        self.password = password

    def save_user(self) :
        """
        save_user method saves user object into users list.
        """
        User.user_list.append(self)

    def delete_user(self) :
        """
        delete user method removes unwanted user object from users list
        """
        User.user_list.remove(self)

    @classmethod #decorator
    def find_by_accountName(cls, accountName) :
        """
        find by accountName method  that takes in the accountname and returns the user tha matches that user password.
        
        Args:
            accountName to search for
        Returns :
            user of the person that matches tha password

        """
        for user in cls.user_list :
            if user.accountName == accountName :
                return user

    @classmethod # decorator
    def user_exist (cls, email) :
        """
        user exist method that checks if the user exist

        Args :
            search if the username exist
        
        Return :
            if the user does not exist the return with boolean
        """
        for user in cls.user_list:
            if user.email == email:
                return True
        return False
    



