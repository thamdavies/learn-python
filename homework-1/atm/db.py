import csv

def users():
    users = []
    with open('atm/data/users.csv', newline='') as csvfile:
        csvfile.seek(0)
        reader = csv.DictReader(csvfile)
        for row in reader:
            user = {'name': row['name'], 'account_balance': row['account_balance'], 'username': row['username'], 'pin_code': row['pin_code']}
            users.append(user)

    return users
