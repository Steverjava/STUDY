username = str(input("Please enter your username: "))
password = str(input("Please enter your password: "))

UserName = "Steverjava"
Password = "123456"

if username == UserName:
    if password == Password:
        print("You are logged in!")
    else:
        print("You are not logged in!")
else:
    print("You are not logged in!")
