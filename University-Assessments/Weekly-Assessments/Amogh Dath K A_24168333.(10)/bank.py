## LAB ASSIGNMENT :- 9 ( WEEK 9 LAB ACTIVITY 1)
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################
# TO FORM A BANKING SYSTEM AND PERFORMING SOME FUNCTIONS BY COMPLETING THE TO DO BY PASSES IN THE GIVEN ASSIGNMENT #

# CODE STARTING #
# Bank System - Simplified Version and compact and completed version.. completed all the to do bypasses #
# Bank System - Debugging Version

# Customer Class
class Customer:
    def __init__(self, cID, first_name, second_name, address, balance):
        print("Initializing Customer")
        self.__cID = cID
        self.__first_name = first_name
        self.__second_name = second_name
        self.__address = address
        self.__balance = balance

    def get_cID(self):
        return self.__cID

    def set_cID(self, c_id):
        self.__cID = c_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, f_name):
        self.__first_name = f_name

    def get_second_name(self):
        return self.__second_name

    def set_second_name(self, s_name):
        self.__second_name = s_name

    def get_address(self):
        return self.__address

    def set_address(self, addObj):
        self.__address = addObj

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def check_balance(self):
        return self.__balance


# Address Class
class Address:
    def __init__(self, number, street, town, post_code):
        print("Initializing Address")
        self.__number = number
        self.__street = street
        self.__town = town
        self.__post_code = post_code

    def get_number(self):
        return self.__number

    def set_number(self, value):
        self.__number = value

    def get_street(self):
        return self.__street

    def set_street(self, value):
        self.__street = value

    def get_town(self):
        return self.__town

    def set_town(self, value):
        self.__town = value

    def get_post_code(self):
        return self.__post_code

    def set_post_code(self, value):
        self.__post_code = value

    def change_address(self, new_address):
        self.__number = new_address.get_number()
        self.__street = new_address.get_street()
        self.__town = new_address.get_town()
        self.__post_code = new_address.get_post_code()

    def __str__(self):
        return f"{self.__number},{self.__street},{self.__town},{self.__post_code}"


# Function to create a new customer
def new_customer():
    print("Creating new customer")
    cid = int(input("Enter customer id number: "))
