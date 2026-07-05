num = 0
a = 0
b = 0

while num < 10:

    number = int(input("Enter a number: "))
    num +=1

    if number > 0:
        a +=1
    elif number < 0:
        b +=1
    else:
        continue

print(f"There are {a} positive numbers,{b} negative numbers.")
