money = 1000

while True:
    print(" 1. Check Balance\n","2. Deposit\n","3. Withdraw\n","4. Exit")
    num = input("Enter your choice: ")
    if num == "1":
        print("Your balance is ",money)
    elif num == "2":
        add_money = int(input("How much money would you like to add?"))
        money += add_money
        print("get it.")
    elif num == "3":
        reduce_money = int(input("How much money would you like to withdraw?"))
        money -= reduce_money
        print("get it.")
    elif num == "4":
        break
    else:
        print("Please enter a valid choice.")
        continue
