# Intermediate and Challenging ----------------------------------------------------------------------------------------------------------?
# Part A — Intermediate Problems ---------------------------------------------------------------------------?
# Q=1 -----------------------------------------------------------?
marks = int(input("Enter Your marks => "))
while marks < 0 or marks > 100:
    print("Invalid marks")
    marks = int(input("Enter Your marks =>  "))
else:
    print("Accepted marks =>", marks)


# Q=2 -----------------------------------------------------------?
num = int(input("Enter a positive integer => "))
while num <= 0:
    print("Number must be greater than 0.")
    num = int(input("Enter a positive integer => "))
else:
    print("Accepted number => ", num)


# Q=3 --------------------------------------------------------------?
age = int(input("Enter your age => "))
while age < 0 or age > 120:
    print("Invalid age")
    age = int(input("Enter your age => "))
else:
    print("Accepted age =>", age)


# Q=4 ------------------------------------------------------------?
choice = int(input("Enter your choice => "))
match choice:
    case 1:
        print("View profile")
    case 2:
        print(" Edit profile")
    case 3:
        print(" Settings")
    case 4:
        print(" Exit")
    case _:
        print("Invalid Menu Choice")


# Q=5 ----------------------------------------------------------------?
Password = input("Enter Your Password => ").strip()
while len(Password) < 8:
    print("Too short")
    Password = input("Enter Your Password => ").strip()
else:
    print("Password accepted")


# Q=6 ----------------------------------------------------------------?
Tem = float(input("Enter Your Temperature => "))
while Tem < -20 or Tem > 45:
    print("Invalid temperature")
    Tem = float(input("Enter Your Temperature => "))
else:
    print("Accepted =>", Tem)


# Q=7 --------------------------------------------------------------------?








