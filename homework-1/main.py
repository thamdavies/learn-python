import csv
import os
from user import User

users = []
with open('./data/users.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, quotechar='|')
    csvfile.seek(0)
    reader = csv.DictReader(csvfile)
    for row in reader:
        user = User(row['name'], row['account_balance'], row['pin_code'])
        users.append(user)


choice = ''
def display_menu():
    print("Welcome to the Bank of Python")
    print("1. Withdrawal")
    print("2. Transfer")
    print("3. Check Balance")
    print("4. Export data (CSV, Excel, PDF)")
    print("5. User details")
    print("6. User list")
    global choice
    choice = input("Enter your choice: ")


while choice != 'exit':
    display_menu()
    if choice == '1':
        os.system('clear')
        name = input("Enter your name: ")
        pin_code = input("Enter your pin code: ")
        amount = int(input("Enter amount: "))
        for user in users:
            if user.name == name and user.pin_code == pin_code:
                user.make_withdrawal(amount)
                print(f"User: {user.name}, Balance: ${user.account_balance}")
    elif choice == '2':
        os.system('clear')
        name = input("Enter your name: ")
        pin_code = input("Enter your pin code: ")
        amount = int(input("Enter amount: "))
        for user in users:
            if user.name == name and user.pin_code == pin_code:
                user.make_deposit(amount)
                print(f"User: {user.name}, Balance: ${user.account_balance}")
    elif choice == '3':
        os.system('clear')
        name = input("Enter your name: ")
        pin_code = input("Enter your pin code: ")
        for user in users:
            if user.name == name and user.pin_code == pin_code:
                print(f"User: {user.name}, Balance: ${user.account_balance}")
    elif choice == '4':
        os.system('clear')
        name = input("Enter your name: ")
        pin_code = input("Enter your pin code: ")
        for user in users:
            if user.name == name and user.pin_code == pin_code:
                user.export_data()
    elif choice == '5':
        os.system('clear')
        name = input("Enter your name: ")
        pin_code = input("Enter your pin code: ")
        for user in users:
            if user.name == name and user.pin_code == pin_code:
                user.user_details()
    elif choice == '6':
        os.system('clear')
        for user in users:
            user.print_info()
    else:
        os.system('clear')
        print("See you next time!")
        break

# - Viết một chương trình Python để mô phỏng các tính năng của một máy ATM, bao gồm:
#     1. Rút tiền
#     2. Chuyển khoản
#     3. Kiểm tra số dư
#     4. Xuất ra file CSV, Excel, PDF
#     5. Truy xuất thông tin người dùng thông qua API
#     6. Hiển thị danh sách người dùng
# - Tương tác với người dùng qua Terminal, hiển thị banner menu và cho phép chọn số tương ứng
# - Xác thực người dùng bằng tên và mã pin trước khi thực hiện các tính năng
# - Sử dụng một danh sách user được tạo sẵn, mỗi user có tên, số dư và mã pin.
#     - Tạo file Yaml để dump dữ liệu. Khi chạy chương trình sẽ load file dump
# - Kiểm tra điều kiện và báo lỗi khi cần
# - Sử dụng các thư viện sau để xuất ra file và truy xuất API, Ví dụ:
#     - csv
#     - xlsxwriter
#     - fpdf
#     - requests
# - Có vòng lặp chính để xử lý các lựa chọn của người dùng và có thể thoát khi nhập `exit`
# - Code theo hướng OOP
