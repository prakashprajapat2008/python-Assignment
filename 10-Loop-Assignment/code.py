#Practice Problems
#A. Basic for Loop
#Q=1 Write a program to print "Hello" five times using a for loop.
for i in range(5):
    print("Hello")


#Q=2 Print the numbers:
for i in range(0,10):
    print(i, end=" ")


#Q=3 Print the numbers from 1 to 10.
for i in range(1,11):
    print(i, end="")


#Q=4 Print the numbers from 10 to 1 in reverse order.
for i in range(10,0,-1):
    print(i, end=" ")


#Q=5 Print the numbers from 5 to 50, increasing by 5.
for i in range(5,51):
    if i %5==0:
        print(i, end=" ")


#B. range() Practice
#Q=6 Print all even numbers from 2 to 20 using range().
for i in range(2,21):
    if i %2==0:
        print(i, end=" ")


#Q=7 Print all odd numbers from 1 to 19 using range().
for i in range(1,20):
    if i %2==1:
        print(i, end=" ")


#Q=8 Print the numbers:
for i in range(3,19):
    if i %3==0:
        print(i, end="")


#Q=9 Print the numbers from 20 down to 2, decreasing by 2.
for i in range(20,0,-1):
    if i %2==0:
        print(i, end=" ")


#Q=10 Take a positive integer n from the user and print all numbers from 1 to n.
n = int(input("Enter your Nomber:"))
for i in range(1,n+1):
    print(i, end=" ")


#C. Conditions with for
#Q=11 Take n from the user and print only the even numbers from 1 to n.
n = int(input("Enter your Number:"))
for i in range(1,n+1):
    if i %2==0:
        print(i, end=" ")


#Q=12 Take n from the user and print only the odd numbers from 1 to n.
n = int(input("Enter your Number:"))
for i in range(1,n+1):
    if i %2==1:
        print(i, end=" ")


#Q=13 Take n from the user and print all numbers from 1 to n that are divisible by 3.
n = int(input("Enter your Number:"))
for i in range(1,n+1):
    if i %3==0:
        print(i, end=" ")


#Q=14 Take n from the user and print all numbers from 1 to n that are divisible by both 2 and 3.
n = int(input("Enter your Number:"))
for i in range(1,n+1):
    if i %2==0 and i %3==0:
        print(i, end=" ")


#Q=15 Take n from the user and count how many numbers from 1 to n are even.
n = int(input("Enter your Number:"))
count = 0
for i in range(1,n+1):
    if i %2==0:
        count = count+1
print("Total Even Number is count:", count)


#D. Calculation Problems
#Q=16 Take n from the user and calculate:
n = int(input("Enter your Number:"))
count = 0
for i in range(1,n+1):
    count = count+i
print("Total Number is Sum count:", count)


#Q=17 Take n from the user and calculate the sum of all even numbers from 1 to n.
n = int(input("Enter your Number:"))
count = 0
for i in range(1,n+1):
    if i %2==0:
        count = count+i
print("Total Even Number is Sum count:", count)


#Q=18 Take n from the user and calculate the sum of all odd numbers from 1 to n.
n = int(input("Enter your Number:"))
count = 0
for i in range(1,n+1):
    if i %2==1:
        count = count+i
print("Total Odd Number is Sum count:", count)


#Q=19 Take a number from the user and print its multiplication table from 1 to 10.
n = int(input("Enter your Number:"))
for i in range(1,11):
        print(f"{n} * {i}  = {n*i}")


#Q=20 Take a number n and calculate:
n = int(input("Enter your Number:"))
count = 1
for i in range(1,n+1):
    count = count*i
print("Total Number is product count:", count)


#E. String Iteration
#Q=21 Take a string from the user and print each character on a separate line.
Word = input("Enter your string:")
for i in Word:
    print(i)


#Q=22 Take a string from the user and print all its characters on the same line using end="".
Word = input("Enter Your string:")
for i in Word:
    print(i, end=" ")


#Q=23 Take a string from the user and count the number of characters in it using a for loop.
Word = input("Enter Your string:")
count = 0
for i in Word:
    count = count+1
print("chararacte:",count)


#Q=24 Take a string from the user and count how many times the character "a" appears.
word = input("Enter Your string:")
count = 0
for i in word:
    if i == "a":
        count = count + 1
print("chararacte:", count)


#Q=25 Take a string from the user and count how many characters are uppercase letters.
word = input("Enter Your string:")
count = 0
for i in word:
    if i>="A" and i<="Z":
        count = count + 1
print("Uppercase chararacte:", count)


#F. Nested for Loops
#Q=26 Use nested loops to print:
for row in range(3):
    for column in range(4):
        print("*", end="")
    print()


#Q=27 Use nested loops to print:
for row in range(4):
    for column in range(4):
        print("*", end="")
    print()


#Q=28 Print the following pattern:
for row in range(1, 6):
    for column in range(1, row + 1):
        print("*", end="")
    print()


#Q=29 Print the following pattern:
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end="")
    print()


#Q=30 Create a multiplication-table grid using nested for loops.?For example, for numbers 1 to 5, produce rows showing their multiplication results.
for row in range(5):
    for column in range(5):
        print((row+1)*(column+1), end="\t")
    print()

#Final Practice Challenge
#Try to solve the following without copying an earlier example.
n = int(input("Enter your Number:"))
for row in range(1, n+1):
    for column in range(1, row + 1):
        print(column, end="")
    print()


