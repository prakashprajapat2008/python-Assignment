#Part 3 — Practical Programs
#Task 1-Basic Arithmetic
a = 10
b = 5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

#Task 2 — Integer and Float
a = 10
b = 5.5
#The result
print("Addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("Division:", a/b)
print("Floor division:", a//b)
print("Modulus:", a%b)
print("Exponentiation:", a**b)
#The data type of the result
print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/b))
print(type(a//b))
print(type(a%b))
print(type(a**b))

#Task 3 — Student Marks
maths = 80
physics = 70
chemistry = 75
#Product price
Total = maths + physics + chemistry
print("Total marks:", Total)
#Average marks
average = Total/3
print("Average marks:", average)

#Task 4 — Product Calculation
Product_price = 100
Quantity = 10
Total_price = Product_price*Quantity 
print("total price=", Total_price)

#Task 5 — Even or Odd
number = 15
if number % 3 == 0:
    print("Even")
else:
    print("Odd")

#Task 6 — Division and Floor Division
a = 15
b = 8
Normal_division = a/b
Floor_division = a//b
print("Normal division:", Normal_division )    
print("Floor division:", Floor_division)

#Task 7 — Negative Number Operations
a = -20
b = -5
print("Addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("Division:", a/b)
print("Floor division:", a//b)
print("Modulus:", a%b)

#Task 8 — Subtraction Edge Cases
a = 12
b = 10
print("positive - positive:", a-b)
print("positive - negative:", a-(-b))
print("negative - positive:", (-a)-b)
print("negative - negative:", (-a)-(-b))

#Task 9 — Floor Division Edge Cases
a = 8
b = 15
print(a//b)
print((-a)//b)
print(a//(-b))
print((-a)//(-b))

#Task 10 — Modulus Edge Cases
a = 8
b = 15
print(a%b)
print((-a)%b)
print(a%(-b))
print((-a)%(-b))

#Part 4 — Operator Precedence
#Task 11
print(10 + 5 * 2)
print(20 - 4 / 2)
print(10 + 20 / 5 * 2)
print(2 + 3 * 4 ** 2)
print(100 - 20 // 5)

#Task 12 — Parentheses
a = 10
b = 5
c = 2
print(a+b*c)
print((a+b)*c)
a = 20
b = 10
c = 2
print(a-b/c)
print((a-b)/c)
a = 2
b = 3
c = 4
print(a+b*c)
print((a+b)*c)

#Part 5 — Boolean Arithmetic
#Task 13
a = 1
b = 0
print("Addition:", a+b)
print("subtraction:", a-b)
print("multiplication:", a*b)
print("Division:", a/(b+True))
print("Floor division:", a//(b+True))
print("Modulus:", a%(b+True))
print("Exponentiation:", a**(b+True))
print(type(a+b))
print(type(a-b))
print(type(a*b))
print(type(a/(b+True)))
print(type(a/(b+True)))
print(type(a/(b+True)))
print(type(a/(b+True)))

#Task 14
print(True + 5)
print(False + 5)
print(True * 10)
print(False * 10)
print(True - 5)
print(False - 5)

#Part 6 — String Operations
#Task 15
First_Name = "prakash"
Last_Name = "kailash"
full_name = First_Name + " " + Last_Name
print(full_name)

#Task 16
name="Prakash"
lname="prajapat"
print("Outpute for task-16:",(name+" "+lname)*4)

#Task 17
name="prakash"
lname="prajapat"
print("Outpute for task-17:",name+" "+lname,(name+" "+lname)*4)
print("The subtraction and division show the Type error.....")

#Part 7 — None Type
#Task 18
value = None
num=12
print("Outpute for task-18:"," Python show -TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'")

#Part 8 — Error Handling Practice
#Task 19
x=10000000
y=0
print("Outpute for task-19:","Python shows - ZeroDivisionError: division by zero")

#Task 20 — Mini Calculator
num1 = 10
num2 = 5

print("Outpute for task-20:","Addition: ...",num1 + num2)
print("Outpute for task-20:","Subtraction: ...",num1 - num2)
print("Outpute for task-20:","Multiplication: ...",num1 * num2)
print("Outpute for task-20:","Division: ...",num1 / num2)
print("Outpute for task-20:","Floor Division: ...",num1//num2)
print("Outpute for task-20:","Modulus: ...",num1%num2)
print("Outpute for task-20:","Exponentiation: ...",num1**num2)

#Part 10 — Final Challenge
#Task 21 — Arithmetic Expression Analyzer
a = 10
b = -3
c = 2.5
print("Outpute for task-21:")
print(a + b)
print(a - b)
print(a * c)
print(a / c)
print(a // b)
print(a % b)
print(a ** 2)
print((a + b) * c)
print(a + b * c)
print((a - b) / c)
print(a ** 2 + b * c)
print((a + c) // 2)