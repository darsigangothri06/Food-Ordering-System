from sys import exit
from prettytable import PrettyTable

def Exit(s):
    if s == 'exit':
        print('---------------ThankYou---------------')
        exit()
def password_valid(s):
    if len(s) not in range(8,13):
        print("Minimum length of password is 8 and maximum length is 12")
        return False
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
    return False
    
def username_valid(s):
    for i in s:
        if not i.isalpha():
            return False
    with open("user_data.txt","r") as f:
        for i in f.readlines():
            p = i.split()
            if len(p) == 5 and p[0] == s:
                return False
        return True

def emailid_valid(s):
    with open("user_data.txt","r") as f:
        for i in f.readlines():
            p = i.split()
            if len(p) == 5 and p[2] == s:
                return False
    if '@' in s:
        return True
    return False

def username_input():
    username = input("Enter valid username: ")
    Exit(username)
    if username_valid(username):
        return username
    else:
        print("Invalid username, enter again")
        return username_input()       

def age_input():
    age = int(input("Enter your age: "))
    if age > 0:
        return age
    print("Invalid age, Enter again")
    return age_input()

def email_input():
    emailid = input("Enter your email id: ")
    Exit(emailid)
    if emailid_valid(emailid):
        return emailid
    else:
        print("Emailid is taken/invalid, Enter again")
        return email_input()

def password_input():
    password = input("Enter your password: ")
    Exit(password)
    password_retype = input("Re-enter your password: ")
    Exit(password_retype)
    if password == password_retype:
        if password_valid(password):
            return password
        else:
            print("Invalid password, enter again")
            return password_input()
    else:
        print("Password is invalid, Signup again")
        return password_input()

def mobile_input():
    number = input("Enter your mobile number: ")
    Exit(number)
    if len(number) != 10:
        print("Please enter valid mobile number")
        return mobile_input()
    for i in number:
        if not i.isdigit():
            print("Please enter valid mobile number")
            return mobile_input()
    return number

def login_check(userid,password):
    if '@' in userid:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if p[2] == userid:
                    if p[3] == password:
                        print("Congrats {}, You have successfully logged into your account".format(p[0]))
                        return Order()
                    else:
                        print("Incorrect password, try again")
                        return login()
            else:
                print("Emailid not found, please signup to continue")
                return Start()
    else:
        with open("user_data.txt","r") as f:
            for i in f.readlines():
                p = i.split()
                if p[0] == userid:
                    if p[3] == password:
                        print("Congrats {}, You have successfully logged into your account".format(p[0]))
                        return Order()
                    else:
                        print("Incorrect password")
                        password = input("Enter password: ")
                        Exit(password)
                        return login_check(userid,password)
            print("Username not found, please Login/Signup to continue")
            return Start()

def signup():
    print('-'*20 + "Signup" + '-'*20)
    user_name = username_input()
    age = age_input()
    emailid = email_input()
    password = password_input()
    mobile_number = mobile_input()
    with open("user_data.txt","a") as file:
        file.write('\n' + user_name + ' ' + str(age) + ' ' + emailid + ' ' + password + ' ' + mobile_number)
    print("Congratulations, you have successfully created your account..")
    print("You can now login to your account")
    print()
    return Start()

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
        return login()
    password = input("Enter password: ")
    Exit(password)
    login_check(userid,password)

def Cart(Cart_Items):
    Cart_Table = PrettyTable(['S. no', 'Item','Item Cost', 'Count', 'Amount'])
    cost = 0
    c = 1
    for i in Cart_Items:
        Cart_Table.add_row([str(c) + '.', str(i[0]), str(i[1]), str(i[2]), str(i[1]  * i[2])])
        cost += i[1] * i[2]
        c += 1
    print(Cart_Table)
    print("\n Total Amount is: ", cost, '\n')
    p = int(input("Do you want to order (y = 1/n = 0): "))
    if p == 1:
        print("\nThankyou, Your order is on the way. Welcome Again")
        exit()
    else:
        print("Your order is cancelled. Thankyou!!")
        exit()

cost = 0
Cart_items = []
def Available(Items):
    Table = PrettyTable(['S. No','Item','Cost (Rs.)'])
    global cost
    print("-----------------Available Items are-------------------\n")
    c = 1
    for i in Items:
        Table.add_row([str(c) + '.',i[0],i[1]])
        c += 1
    print(Table)
    print("Cart (Type Cart)")
    print("Exit (Type Exit)")
    del Table
    ans = input("Enter: ")
    if ans == "Exit" or ans == "exit":
        exit()
    if ans == "Cart" or ans == "cart":
        Cart(Cart_items)
    else:
        x = int(input("Enter the count of your item: "))
        cost += Items[int(ans)-1][1]*x
        Cart_items.append([Items[int(ans) - 1][0], Items[int(ans) - 1][1], x])
        Available(Items)

def HMourya():
    Food_Price = [['Parrota',15], ['Roti',25], ['Shangrilla',150], ['Biryani',40], ['Noodles',70]]
    Available(Food_Price)
def HAFC():
    Food_Price = [['Roti',15], ['Manchuria',45], ['Noodles',150], ['Biryani',40], ['Fried Rice',70]]
    Available(Food_Price)
def HSM():
    Food_Price = [['Roti',15], ['Manchuria',45], ['Noodles',150], ['Biryani',40], ['Fried Rice',70]]
    Available(Food_Price)
def HTSC():
    Food_Price = [['Mushroom Shawarma',15], ['Manchurian Shawarma',45], ['Egg Shawarma',150], ['Chicken Shawarma',40], ['Baby Corn Shawarma',70]]
    Available(Food_Price)
def HVRP():
    Food_Price = [['Roti',15], ['Manchuria',45], ['Noodles',150], ['Biryani',40], ['Fried Rice',70]]
    Available(Food_Price)

def OrderByFood():
    print("----------------Order By Food--------------\n")
    Food_Price = [['Roti',15], ['Manchuria',45], ['Noodles',150], ['Biryani',40], ['Fried Rice',70],['Chocolate Ice Cream',99],['Food1',110],['Food2',120],['Food3',100],['Food4',50]]
    Available(Food_Price)
    
def OrderByHotel():
    print("-------------------Order By Hotel---------------\n")
    print("""----------------Available Hotels are--------------\n""")
    NewTable = PrettyTable(['S. No', 'Hotel'])
    NewTable.add_row(['1. ', 'Mourya'])
    NewTable.add_row(['2. ', 'Amaravathi Food Court'])
    NewTable.add_row(['3. ', 'Sweet Magic'])
    NewTable.add_row(['4. ', 'The Shawarma Co.'])
    NewTable.add_row(['5. ', 'V Royal Park'])
    print(NewTable)
    ans = input("Enter your choice (1-5): ")
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
    ans = input("""-------Welcome to your account-------
1. Order by hotel
2. Order by Food
3. Exit

Enter here: """)
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

Enter here: """)
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
