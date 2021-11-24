from sys import exit

def Exit(s):
    if s == 'exit':
        print('ThankYou')
        exit()
def password_valid(s):
    if len(s) not in range(8,13):
        print("Minimum length of password is 8 and maximum length is 12, Re-enter your password")
        password_input()
    Upper = 0
    Digit = 0
    Lower = 0
    Special = 0
    for i in s:
        if i == i.upper():
            Upper = 1
        if i.isdigit():
            Digit = 1
        if i == i.lower():
            Lower = 1
        if i in ['!', '@', '#', '$', '%', '^', '&', '*','.']:
            Special = 1
    if Upper and Lower and Digit and Special:
        return True
    print("Password is invalid, Re-enter again")
    password_input()
    
def username_valid(s):
    for i in s:
        if not i.isalpha():
            print("Username is invalid, Re-enter again")
            username_input()
    for i in s:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if len(p) == 5 and p[0] == s:
                    print("Username is already taken, enter new username")
                    username_input()
    return True

def emailid_valid(s):
    for i in s:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if len(p) == 5 and p[2] == s:
                    print("Eamilid is already taken, Re-enter new emailid")
                    email_input()
    if '@' in s:
        return True
    print("Emailid is invalid, Re-enter again")
    email_input()

def username_input():
    username = input("Enter valid username: ")
    Exit(username)
    if username_valid(username):
        return username
    print("Invalid username")
    exit()

def age_input():
    age = int(input("Enter your age: "))
    if age > 0:
        return age
    print("Invalid age")
    exit()

def email_input():
    emailid = input("Enter your email id: ")
    Exit(emailid)
    if emailid_valid(emailid):
        return emailid
    return False

def password_input():
    password = input("Enter your password: ")
    Exit(password)
    password_retype = input("Re-enter your password: ")
    Exit(password_retype)
    if password == password_retype:
        if password_valid(password):
            return password
    print("Password is invalid, Signup again")
    password_input()

def mobile_input():
    number = input("Enter your mobile number: ")
    Exit(number)
    if len(number) != 10:
        print("Please enter valid mobile number")
        mobile_input()
    for i in number:
        if not i.isdigit():
            print("Please enter valid mobile number")
            mobile_input()
    return number

def login_check(userid,password):
    if '@' in userid:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if len(p) == 5 and p[2] == userid:
                    if p[3] == password:
                        print("Congrats {}, You have successfully logged into your account".format(p[0]))
                        Order()
                    else:
                        print("Incorrect password, try again")
                        exit()
            print("Emailid not found, please signup to continue")
            exit()
    else:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if len(p) == 5 and p[0] == userid:
                    if p[3] == password:
                        print("Congrats {}, You have successfully logged into your account".format(p[0]))
                        Order()
                    else:
                        print("Incorrect password")
                        password = input("Enter password: ")
                        Exit(password)
                        login_check(userid,password)
            print("Username not found, please signup to continue")
            print('-'*50)
            exit()

def signup():
    print('-'*20 + "Welcome" + '-'*20)
    username = username_input()
    age = age_input()
    emailid = email_input()
    password = password_input()
    mobile_number = mobile_input()
    with open("user_data.txt","a") as file:
        file.write(username + ' ' + str(age) + ' ' + emailid + ' ' + password + ' ' + mobile_number + '\n')
    print("Congratulations, you have successfully created your account..")
    print("You can now login to your account")
    print()
    Start()

def login():
    ans = input("Do you want to enter username or email (1 or 2): ")
    Exit(ans)
    if ans == '1':
        userid = input("Enter username: ")
        Exit(ans)
    elif ans == '2':
        userid = input("Enter emailid: ")
        Exit(ans)
    else:
        print("Enter valid input")
        exit()
    password = input("Enter password: ")
    Exit(password)
    login_check(userid,password)

def Start():
    print("Food Ordering System!! If you want to exit at any time, please type exit")
    ans = input("""
1. Signup
2. Login
3. Exit
""")
    Exit(ans)
    if ans == '1':
        signup()
    elif ans == '2':
        login()
    elif ans == '3':
        exit()
    else:
        print("Enter valid input")

Start()
