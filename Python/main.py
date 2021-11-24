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
                        break
                    else:
                        print("Incorrect password, try again")
                        exit()
            else:
                print("Emailid not found, please signup to continue")
                Start()
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
    print('-'*20 + "Signup" + '-'*20)
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

cost = 0
def Available(Items):
    global cost
    print("------Available Items are-----")
    for i in Items:
        print("{0:25} Rs. {1:-3}".format(i[0],i[1]))
    print("Cart (Type Cart)")
    print("Exit (Type Exit)")
    ans = input("Enter: ")
    if ans == "Exit" or ans == "exit":
        exit()
    if ans == "Cart" or ans == "cart":
        print("------------Cart------------")
        print("Your total amount is ", cost)
        p = int(input("Do you want to order (y = 1/n = 0): "))
        if p == 1:
            print("Thankyou, Your order is on the way. Welcome Again")
            exit()
        else:
            print("Your order is cancelled.")
            exit()
    else:
        x = int(input("Enter the count of your item: "))
        cost += Items[int(ans)-1][1]*x
        Available(Items)

def HMourya():
    Food_Price = [['1. Parrota',15], ['2. Roti',25], ['3. Shangrilla',150], ['4. Biryani',40], ['5. Noodles',70]]
    Available(Food_Price)
def HAFC():
    Food_Price = [['1. Roti',15], ['2. Manchuria',45], ['3. Noodles',150], ['4. Biryani',40], ['5. Fried Rice',70]]
    Available(Food_Price)
def HSM():
    Food_Price = [['1. Roti',15], ['2. Manchuria',45], ['3. Noodles',150], ['4. Biryani',40], ['5. Fried Rice',70]]
    Available(Food_Price)
def HTSC():
    Food_Price = [['1. Mushroom Shawarma',15], ['2. Manchurian Shawarma',45], ['3. Egg Shawarma',150], ['4. Chicken Shawarma',40], ['5. Baby Corn Shawarma',70]]
    Available(Food_Price)
def HVRP():
    Food_Price = [['1. Roti',15], ['2. Manchuria',45], ['3. Noodles',150], ['4. Biryani',40], ['5. Fried Rice',70]]
    Available(Food_Price)

def OrderByFood():
    print("---------Order By Food--------")
    Food_Price = [['1. Roti',15], ['2. Manchuria',45], ['3. Noodles',150], ['4. Biryani',40], ['5. Fried Rice',70],['6. Chocolate Ice Cream',99],['7. Food1',110],['8. Food2',120],['9. Food3',100],['10. Food4',50]]
    Available(Food_Price)
    
def OrderByHotel():
    print("---------Order By Hotel-------")
    ans = input("""Available Hotels are
1. Mourya
2. Amaravathi Food Court
3. Sweet Magic
4. The Shawarma Co.
5. V Royal Park
Enter your choice: """)
    if ans == '1':
        HMourya()
    elif ans == '2':
        HAFC()
    elif ans == '3':
        HSM()
    elif ans == '4':
        HTSC()
    elif ans == '5':
        HVRP()
    else:
        print("Enter valid input")
        OrderByHotel()

def Order():
    ans = input("""Food Order System
1. Order by hotel
2. Order by Food
3. Exit
""")
    Exit(ans)
    if ans == '1':
        OrderByHotel()
    elif ans == '2':
        OrderByFood()
    elif ans == '3':
        exit()
    else:
        print("Enter valid input")
        Order()

def Start():
    print("------------------FOOD ORDERING SYSTEM-----------------")
    print("If you want to exit at any time, please type exit")
    ans = input("""1. Signup
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
Start()
