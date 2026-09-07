#Practice Problems
#A. Basic if
#Q=1 Write a program that checks whether a number is greater than 10. If it is, print:
is_number = 20
if is_number > 10:
    print("Greater than 10")

#Q=2 Write a program that checks whether a person's age is at least 18. If true, print:
age = 25
if age >= 18:
    print("Adult")

#Q=3 Take a number from the user and print Positive if the number is greater than 0.
is_number = int(input("Enter a number: "))
if is_number > 0:
    print("Positive")

#Q=4 Write an if statement that checks whether:
is_marks = 80
if is_marks >= 40:
    print("Pass")

#Q=5 Take a number from the user and print Zero when the number is equal to 0.
is_number = int(input("Enter a number: "))
if is_number == 0:
    print("Zero")

#B. if-else
#Q=6 Write a program that checks whether a number is positive or not.
is_number = int(input("Enter a number: "))
if is_number > 0:
    print("Positive")
else:
    print("Not positive")

#Q=7 Take a person's age and display:
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Q=8 Write a program that checks whether a number is even or odd using %.
is_number = int(input("Enter a number: "))
if is_number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q=9 Take marks from the user and display Pass if marks are at least 40; otherwise display Fail.
is_marks = int(input("Enter marks: "))
if is_marks >= 40:
    print("Pass")
else:
    print("Fail")

#Q=10 Take two numbers and print which one is greater using if-else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is greater")
else:
    print("Second number is greater")




































