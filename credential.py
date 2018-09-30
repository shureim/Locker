class Credential :
    """
    class that generate new instance 

    """ 
    credential_list = [] # empty credential list
    """
    method that initialize the credential list 
    """
    def __init__(self, accountName, email, password) :
        """
        __init__ method that help us create properties of the object

            Args :
            accountName : new credential accountName
            email : new credential email
            password : new credential  password
        """
        self.accountName = accountName
        self.email = email
        self.password = password

    def save_credential(self) :
        """
        save_credential method saves credential object into credential list.
        """
        Credential.credential_list.append(self)

    # def delete_credential(self) :
    #     """
    #     method that delete credential from credential list
    #     """
    #     Credential.credential_list.remove(self)

    # @classmethod #decorator
    # def find_by_email(cls, email) :
    #     """
    #     find by email method  that takes in the email and returns the credential that matches that credential password.
        
    #     Args:
    #         email to search for
    #     Returns :
    #         credential of the person that matches that password
    #     """
    #     for credential in cls.credential_list :
    #         if credential.email == email :
    #             return credential

    # @classmethod # decorator
    # def display_credential(cls) :
    #     """
    #     method that returns credential list
    #     """
    #     return cls.credential_list

    # @classmethod # decorator
    # def user_exist (cls, email) :
    #     """
    #     user exist method that checks if the user exist

    #     Args :
    #         search if the username exist
        
    #     Return :
    #         if the user does not exist the return with boolean
    #     """
    #     for user in cls.user_list:
    #         if user.email == email:
    #             return True
    #     return False

   

