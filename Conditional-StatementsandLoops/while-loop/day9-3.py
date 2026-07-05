num = 0
goal = 100

while True:
    string = int(input("Enter a number: "))
    num+=1
    if string == goal:
        break
    elif string > goal:
        print("Grown up")
        continue
    else:
        print("Grown down")
        continue

print(f"You all used {num} times.")
