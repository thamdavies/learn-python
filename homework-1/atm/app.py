import os
from atm.models.user import User
from atm.db import users

class App:
    EXIT_KEYS = ['exit', 'e', '0']

    def __init__(self, name):
        self.__name = name
        self.__users = User.all
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
                self.__withdrawal()
            elif choice == '2':
                self.__transfer()
            elif choice == '3':
              self.__check_balance()
            elif choice == '4':
                print("Export data (CSV, Excel, PDF)")
            elif choice == '5':
               self.__user_details() 
            elif choice == '6':
                self.__user_list()

    # 1. Withdrawal
    def __withdrawal(self):
        try:
            amount = float(input("Enter amount to withdraw: "))
            self.__user.withdraw(amount)
            self.display_menu()
            print("\n")
        except ValueError:
            print("Please enter a number\n")

    # 2. Transfer
    def __transfer(self):
        amount = float(input("Enter amount to transfer: "))
        recipient_username = input("Enter recipient username: ")
        self.__user.transfer(amount, recipient_username)
        self.display_menu()
        print("\n")

    # 3. Check Balance
    def __check_balance(self):
        print(f"\nYour current balance is: {self.__user.fm_account_balance()}\n")
        self.display_menu()
        print("\n")

    # 4. Export data (CSV, Excel, PDF)
    # 5. User details
    def __user_details(self):
        print("\nUser details")
        print(self.__user)
        print("\n")
        self.display_menu()
        print("\n")
    
    # 6. User list
    def __user_list(self):
        print("\nUser list")
        for user in User.all:
            if type(user) is User:
                user.line_printer()
            else:
                User(**user).line_printer()

        print("-" * 37)
        print("\n")
        self.display_menu()
        print("\n")
    
    def __verify_user(self):
        name = input("Enter username: ")
        pin_code = input("Enter your pin code: ")
        user = User.login(name, pin_code)
        if user:
            self.__user = user
            os.system('clear')
            self.__user.greeting(self.__name)
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

