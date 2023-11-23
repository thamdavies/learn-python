import atm.db as db

class User():
    all = db.users()

    def __init__(self, name = '', account_balance = 0, username = '', pin_code = 0, index = -1):
        self.__name = name
        self.__username = username
        self.__account_balance = int(account_balance) 
        self.__pin_code = pin_code
        self.index = index

    @classmethod
    def login(cls, username, pin_code):
        user = cls.find_by_username(username)
        if user and user.pin_code() == pin_code:
            return user 

    @classmethod
    def find_by_username(cls, username):
        for index, user in enumerate(cls.all):
            if user['username'] == username:
                user['index'] = index
                return cls(**user) 

    def pin_code(self):
        return self.__pin_code

    def name(self):
        return self.__name

    def username(self):
        return self.__username

    def account_balance(self):
        return self.__account_balance

    def increase_account_balance(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        print("\n")
        if amount > self.__account_balance:
            print(f"Insufficient funds. Your account balance is {self.fm_account_balance()}\n")
            return self
        elif amount <= 0:
            print("Withdrawal amount must be greater than 0\n")
            return self

        self.__account_balance -= amount
        self.save(self)
        print(f"Withdrawal successful. Your account balance is {self.fm_account_balance()}\n")
        return self

    def transfer(self, amount, recipient_username):
        print("\n")
        if amount > self.__account_balance:
            print(f"Insufficient funds. Your account balance is {self.fm_account_balance()}\n")
            return self
        elif amount <= 0:
            print("Transfer amount must be greater than 0\n")
            return self
        
        user = User.find_by_username(recipient_username)
        
        if user is None:
            print("Recipient not found\n")
            return self
        elif user.username() == self.__username:
            print("You cannot transfer to yourself\n")
            return self

        confirm = input(f"Transfer {amount} to {user.username()}? (y/n): ")
        if confirm != 'y':
            print("Transfer cancelled\n")
            return self

        self.__account_balance -= amount
        user.increase_account_balance(amount)

        self.save(self)
        self.save(user)

        print(f"Transfer successful. Your account balance is {self.fm_account_balance()}\n")
        return self

    def save(self, user):
        User.all[user.index] = user

    def fm_account_balance(self):
        return '${:,}'.format(self.__account_balance)

    def line_printer(self):
        print("-" * 37)
        print(f"| {self.resize_name_width()} | {self.resize_username_width(6)} | {self.resize_account_width(6)} |")
     
    def resize_name_width(self, width = 13):
        return self.name() + (" " * (width - len(self.name())))

    def resize_username_width(self, width = 30):
        return self.username() + (" " * (width - len(self.username())))

    def resize_account_width(self, width = 10):
        return self.fm_account_balance() + (" " * (width - len(self.fm_account_balance())))

    def greeting(self, app_name = 'ATM'):
        print(f"Hi {self.__name}, welcome to the {app_name}")

    def __str__(self):
        return f"Name: {self.__name}\nUsername: {self.__username}\nAccount Balance: {self.fm_account_balance()}"
