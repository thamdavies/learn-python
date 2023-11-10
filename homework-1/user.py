class User:
    def __init__(self, name, email, account_balance):
        self.name = name
        self.email = email
        self.account_balance = account_balance

    def print_info(self):
        print(f"- {self.name}, Email: {self.email}, Balance: ${self.account_balance}")
        return self

    # adding the deposit method
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # adding the withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # adding the display_user_balance method
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    # adding the transfer_money method
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
