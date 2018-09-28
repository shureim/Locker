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


