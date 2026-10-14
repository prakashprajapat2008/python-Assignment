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


# Q=7 -----------------------------------------------------------------?
balance = 5000
bank = int(input("Enter Your Bank => "))
while bank <= 0 or bank > balance:
    bank = int(input("Enter Your Bank => "))
else:
    balance -= bank
    print("Current Balance =>", balance)


# Q=8 ---------------------------------------------------------------?
username = input("Enter Your username => ").strip()
for i in username:
    if i == " ":
        space = True
    else:
        space = False
while len(username) < 5 or space:
    username = input("Enter Your username => ").strip()
else:
    print("Accepted username => ", username)


# Q=9 ----------------------------------------------------------------?
number = int(input("Enter Your number =>  "))
while not (number % 3 == 0 and number % 5 == 0):
    number = int(input("Enter Your number => "))
else:
    print("Accepted number => ", number)


# Q=10 --------------------------------------------------------------?
secret_pin = 2468
for i in range(3):
    pin = int(input("Enter Your pin => "))
    if pin == secret_pin:
        print("PIN accepted")
        break
else:
    print("Access Denied")


# Q=11 ------------------------------------------------------------------?
num = int(input("Enter Your Number => "))
while num < 10 or num > 50:
    num = int(input("Enter Your Number => "))
if num % 2 == 0:
    print(num, "Even")
else:
    print(num, "Odd")


# Q=12 ---------------------------------------------------------------?
balance = 2000
deposit = int(input("Enter Your deposit amount => "))
while deposit <= 0:
    print("Invalid amount")
    deposit = int(input("Enter Your deposit amount => "))
balance = balance + deposit
print("New balance => ", balance)






# Part B — Challenging Problems ----------------------------------------------------------------------------------------------------------?
# Q=13 ----------------------------------------------------------------?
number = -1
while number < 0 or number > 100:
    number = int(input("Enter Your number => "))
else:
    print("Number accepted")


# Q=14 ------------------------------------------------------------------?
marks = -1
while marks < 0 or marks > 100:
    marks = int(input("Enter Your marks => "))
else:
    if marks >= 75:
        print("Distinction")
    elif marks >= 60:
        print("First Class")
    elif marks >= 35:
        print("Pass")
    else:
        print("Fail")


# Q=15 ----------------------------------------------------------------?
username = "b"
password = "b"
for i in username:
    if i == " ":
        space = True
    else:
        space = False
while len(username) < 5 or space or len(password) < 8:
    username = input("Enter Your username => ")
    password = input("Enter Your password => ")
else:
    print("Login Successful")


# Q=16 ----------------------------------------------------------------?
N1 = float(input("Enter Your first Number => "))
op = input("Enter Your operator (+, -, *, /) => ")

while op not in ["+", "-", "*", "/"]:
    op = input("Invalid operator => ")
N2 = float(input("Enter second number => "))

while op == "/" and N2 == 0:
    b = float(input("Enter Your second number => "))
if op == "+":
    result = N1 + N2
elif op == "-":
    result = N1  - N2
elif op == "*":
    result = N1  * N2
else:
    result = N1  / N2

print("Result:", result)


# # Q=17 -------------------------------------------------------------------?
# balance = 10000
# option = -1
# while option != 4:
#     while option < 1 or option > 4:
#         print("""
#     1. Check balance
#     2. Deposit money
#     3. Withdraw money
#     4. Exit
#     """)
#         option = int(input("Select a option => "))
#     else:
#         if option == 1:
#             print(balance)
#         elif option == 2:
#             deposit_amount = -1
#             while deposit_amount < 0:
#                 deposit_amount = int(input("Enter Your deposit => "))
#             else:
#                 balance += deposit_amount
#         elif option == 3:
#             withdrawl_amount = -1
#             while withdrawl_amount < 0 or withdrawl_amount > balance:
#                 withdrawl_amount = int(input("Enter tYour withdrawl => "))
#             else:
#                 balance -= withdrawl_amount
# else:
#     print("Banking Menu Exited")


# Q=18 ----------------------------------------------------------------------------?
month = -1
day = -1
while month < 1 or month > 12 or day > 31 or day < 1:
    month = int(input("Enter Your month => "))
    day = int(input("Enter Your day => "))
else:
    print("Day and Month Accepted")


Q=19 --------------------------------------------------------------------------?












# Q=20 --------------------------------------------------------------------------?
number = int(input("Enter Your range => "))
while number > 20 or number < 1:
    number = int(input("Enter Your range => "))

average = 0
for i in range(number):
    average += int(input("Enter Your number => "))

print(average / number)


Q=21 --------------------------------------------------------------------------?









# Q=22 --------------------------------------------------------------------------?
number = -1
while number < 0 or number > 10:
    number = int(input("Enter Your number => "))
else:
    print("Number Accepted")


# Q=23 --------------------------------------------------------------------------?










# Q=23 --------------------------------------------------------------------------?









