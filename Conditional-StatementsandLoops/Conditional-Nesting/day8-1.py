age = int(input("Enter your age: "))
isVIP = str(input("Do you have a vip? (Y/N): "))

if age >60 or isVIP == "Y":
    print("You can get the off!")
else:
    print("You can not get the off!")
