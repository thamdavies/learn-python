import atm.db as db

class User():
    def __init__(self, name, account_balance, username, pin_code):
        self.name = name
        self.username = username
        self.account_balance = int(account_balance) 
        self.pin_code = pin_code

    @classmethod
    def find_by_username(cls, username):
        users = db.users()
        for user in users:
            if user['username'] == username:
                return cls(**user)

    def __str__(self):
        return f"Name: {self.name}\nUsername: {self.username}\nAccount Balance: {'{:,}'.format(self.account_balance)}"

    def line_printer(self):
        print("-" * 34)
        print(f"| {self.resize_name_width('name')} | {self.resize_name_width('username', 6)} | {self.resize_name_width('account_balance', 6)} |")
     
    def resize_name_width(self, attribute, width = 13):
        return getattr(self, attribute) + (" " * (width - len(getattr(self, attribute))))

