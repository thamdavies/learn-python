import os
from atm.models.user import User
from atm.db import users

class App:
    EXIT_KEYS = ['exit', 'e', '0']

    def __init__(self, name):
        self.__name = name
        self.__users = []
        self.__user = None

    def name(self):
        return self.__name

    def users(self):
        return self.__users

    def run(self):
        print("Login to the ATM")
        self.__verify_user()
        self.__users = users()

        choice = ''
        while choice not in self.EXIT_KEYS:
            choice = input("Enter your choice: ")
            if choice == '1':
                print("Withdrawal")
            elif choice == '2':
                print("Transfer")
            elif choice == '3':
                print("Check Balance")
            elif choice == '4':
                print("Export data (CSV, Excel, PDF)")
            elif choice == '5':
               self.user_details() 
            elif choice == '6':
                print("User list")

    # 1. Withdrawal
    # 2. Transfer
    # 3. Check Balance
    # 4. Export data (CSV, Excel, PDF)
    # 5. User details
    def user_details(self):
        os.system('clear')
        print("|--------- User details ---------|")
        print(self.__user)
        print("\n")
        self.display_menu()
        print("\n")
    
    def __verify_user(self):
        # name = input("Enter username: ")
        # pin_code = input("Enter your pin code: ")
        name = 'tham'
        pin_code = '12345'
        user = User.find_by_username(name)
        if user and user.pin_code == pin_code:
            self.__user = user
            os.system('clear')
            print(f"Hi {user.name}, welcome to the {self.name()}")
            self.display_menu()

        else:
            print("User not found")
            exit()

    def display_menu(self):
        print("1. Withdrawal")
        print("2. Transfer")
        print("3. Check Balance")
        print("4. Export data (CSV, Excel, PDF)")
        print("5. User details")
        print("6. User list")

