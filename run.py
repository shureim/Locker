#!/usr/bin/env python3.6
import random
from user import User 
def create_user(fName, lName, password) :
    """
    to create a new user 
    """
    new_user = User(fName, lName, password)
    return new_user

def save_users(user) :
    """function to save users
    """
    user.save_user()

def del_user(user) :
    """
    function to delete user
    """
    contact.delete_user()

def find_contact(lName) :
    """
    function that finds user  by lastname and returns the contact
    """
    return User.find_by_lastName(lName)

def check_existing_user(lName) :
    """
    function to check if user exist with that lastname and return a boolean
    """
    return User.user_exist(lName)

def display_users():
    """
    function that returns all saved users
    """
    return User.display_user()


def main() :
    print("Hello welcome to your users list. What is your first name?")
    first_Name = input()
    print("Enter second name")
    last_Name = input()
    print(f"Hello {first_Name} {last_Name}. what would you like to do?")
    print('\n')

    while True :
        print("please use this short codes : s - signUp, gg - generate password, l - login, p - save password, fu - find user")
        short_code = input().lower()

        if short_code == "s":
            print("First Name ....")
            fName = input()

            print("Second Name ....")
            lName = input()

            print("Password ....")
            password = input()

            save_users(create_user(fName,lName,password)) # create and save new account
            print('\n')

            print(f"New account {fName} {lName} is created")
            print('\n')

        elif short_code == "gg" :

            print("Enter First Name....")
            fName = input()

            print("Enter Last name......")
            lName = input()
            
            print("password ....")
            username = random.randint(000000,999999) # generated a random password  using the randint method
            password = input(username)

            save_users(create_user(fName,lName,password)) # create and save generated new password
            print('\n')

            print(f" New generated account and password {fName} {lName} {password}")

        elif short_code == "l" :


            print("First Name ....")
            fName = input()

            print("Second Name ....")
            lName = input()

            print("Password ....")
            password = input()
            if password == '1000' :
                print(f"{fName} {lName} has login")
                print('\n')

            else :
                print("you entered the wrong passward")


            save_users(create_user(fName,lName,password)) # create and save login
            print('\n')
            
           


        elif short_code == "p" :
            print("First Name ....")
            fName = input()

            print("Second Name ....")
            lName = input()

            print("Password ....")
            password = input()

            save_users(create_user(fName,lName,password))# save password
            print('\n')
            
            print(f"{fName} {lName} has been saved")
            print('\n')

        elif short_code == "fu":

            print("Enter the user you want to search ")

            search_user = input()
            if check_existing_user(search_user):
                search_user = find_contact(search_user)
                print(f"{search_user.firstName} {search_user.lastName}")
                print('-' * 20)

                print(f"First Name.......{search_user.lastName}")
                print(f"password.......{search_user.user_password}")
            else:
                print("That user does not exist")

        else :
            print("i do not understand what you are saying")

if __name__ == '__main__' :
    main()










      


        
        

   