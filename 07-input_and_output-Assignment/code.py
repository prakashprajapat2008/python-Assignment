#Practice Problems
#A. input() and print()
#Q=1 Write a Python program that asks the user for their name and prints the name.
name = input("Enter your name: ")
print("Your name is:", name)

#Q=2 Write a program that asks the user for their city and displays:
city = input("Enter your city:")
print(f"your city is:{city}")

#Q=3 Take a user's name and age using two separate input() statements and print both values.
name = input("Enter your name:")
age = input("Enter your age:")
print(name)
print(age)

#Q=4 What type of value does input() return by default?
name = input("Enter your name:")
print(type(name))

#Q=5 Write a program that takes a value using input() and displays its type using type().
A = int(input("Enter your A:"))
print(type(A))

#B. Multiple Inputs
#Q=6 Take first name and last name separately and display them together.
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
print(first_name,last_name)

#Q=7 Take three pieces of information:
name = input("Enter your name:")
city = input("Enter your city:")
college = input("Enter your college:")
print(name)
print(city)
print(college)

#Q=8 Write a program that takes two names on the same line and stores them in two variables using .split().
first_name,last_name = input("Enter your two name:").split()
print(first_name)
print(last_name)

#Q=9 Suppose the user enters:
a, b = input("Enter your language:").split()
print("a =", a)
print("b =" ,b)

#Q=10 Write a program that takes three words from one line and displays them separately.
A,B,C = input("Enter your three words:").split()
print(A,B,C)

#C. Type Conversion
#Q=11 Convert the string:
A = "25"
A = int(A)
print(A)
print(type(A))

#Q=12 Convert the string:
A = "25.5"
A = float(A)
print(A)                                    
print(type(A))

#Q=13 Convert the integer:
A = 100
A = str(A)
print(A)
print(type(A))

#Q=14 Take an integer from the user and print its type after conversion.
A = int(input("Enter your integer:")) 
print(A)
print(type(A))

#Q=15 Tak(e a floating-point number from the user and print its type after conversion.
A = float(input("Enter your number:"))
print(A)
print(type(A))

#Q=16 Why does this produce string concatenation instead of numeric addition?
a = input("Enter your number:")
b = input("Enter your number:")
print(a + b)           

#Q=17 Correct the following program so that it performs numeric addition:    
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)

#D. Formatted Output and f-Strings
#Q=18 Create variables:
name = "Rahul"
age = 20
print(f"My name is {name} and I am {age} years old.")

#Q=19Create:
A = 10
B = 20
print(f"The sum is {A + B}")

#Q=20 Take a user's name and age and display them in one sentence using an f-string.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"My name is {name} and I am {age} years old.")

#Q=21 Take the price of a product as a floating-point value and display it using exactly two decimal places.
price = float(input("Enter price: "))
print(f"Price: {price:.2f}")

#Q=22 What is the purpose of:
price = 50.5
print(f"Price: {price:.2f}")

#Q=23 Write a program that takes:
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
print(f"Product: {product_name}")
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")

#E. print() Formatting
#Q=24 What will this display?
print("A", "B", "C")

#Q=25 Rewrite the following so that the values are separated by -:
print("2026", "08", "19")

#Q=26 Write two print() statements that produce:
A = "hello"
B = "world"
print("hello", end=" ")
print("world")

#F. Combined Practice
#Q=27 Write a program that takes two integers from the user and displays:
first_number= int(input("Enter first_number: "))
second_number= int(input("Enter second_number: "))
print(f"First number: {first_number}")
print(f"Second number: {second_number}")
print(f"Sum: {first_number + second_number}")

#Q=28 Write a program that takes the price and quantity of a product and calculates the total cost.
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
total = price * quantity
print(f"Price: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")

#Q=29 Write a program that takes a student's:
name = input("Enter student name: ")
age = int(input("Enter age: "))
marks = float(input("Enter marks: "))
print(f"Student Name: {name}")
print(f"Age: {age}")
print(f"Marks: {marks:.2f}")

#Q=30 Create a small "Student Information" program that:
name = input("Enter student name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")
print("\nStudent Information")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")