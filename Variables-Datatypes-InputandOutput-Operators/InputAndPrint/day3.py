import time

Name = str(input("What is your name? "))
Birthday = str(input("What is your Birthday?(Year) "))
Year = time.strftime("%Y")

Age = int(Year) - int(Birthday)

print("Hello " + Name)
print("And your age is", Age)
