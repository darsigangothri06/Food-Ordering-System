from sys import exit

signup():
    print("------Create new account-------")
    username = input("Enter username: ")
    if check_valid_username():
        password = input("Enter password (case-sensitive): ")
        if check_valid_password():
            print("Congratulations, You have successfully created your account")
            D.update({username:password})
            print("You can now login to your account..")
            Exit = input("Do you want to login or exit (yes or no): ")
            if Exit == 'yes':
                exit()
            else:
                login()

signin():
    username = input("Enter username: ")
    if username in D.keys():
        password = input("Enter password: ")
        if D[username] == password:
            print("You have logged into your account")
            order_by_hotel()
        else:
            print("Enter valid password: ")
            exit()
    else:
        print("Enter valid username")
        exit()

ans = input("Do you want to signup? (yes or no)")
if ans == 'yes':
    signup()
elif ans == 'no':
    signin()
else:
    print("Enter yes or no: ")
    exit()
