# Practice Problems   ----------------------------------------------------------------------------------------?
#A. Basic While Loop   -------------------------------------------------------------------------------------?
# Q=1 Write a program to print "Hello" five times using a for loop
i = 1
while i <= 5:
    print("Hello")
    i = i+1


# Q=2 Print the numbers:
i = 0
while i <= 5:
    print(i ,end=" ")
    i = i+1


# Q=3 Print the numbers from 1 to 10.
i = 1
while i <= 10:
    print(i ,end=" ")
    i = i+1


# Q=4 Print the numbers from 10 to 1 in reverse order.
i = 10
while i >= 1:
    print(i ,end=" ")
    i = i-1


# Q=5 Print the numbers from 5 to 50, increasing by 5.
i = 5
while i <= 50:
    print(i ,end=" ")
    i = i+5



# B. range() Practice  -------------------------------------------------------------------------------------------------------------?
# Q=6 Print all even numbers from 2 to 20 using range().
i = 2
while i <= 20:
    print(i ,end=" ")
    i = i+2


# Q=7 Print all odd numbers from 1 to 19 using range().
i = 1
while i <= 19:
    print(i ,end=" ")
    i = i+2


# Q=8 Print the numbers:
i = 3
while i <= 18:
    print(i ,end=" ")
    i = i+3


# Q=9 Print the numbers from 20 down to 2, decreasing by 2.
i = 20
while i >= 2:
    print(i ,end=" ")
    i = i-2


# Q=10 Take a positive integer n from the user and print all numbers from 1 to n.
n = int(input("Enter your Number =>"))
i = 1
while i <= n:
    print(i ,end=" ")
    i = i+1




# C. Conditions with for  ------------------------------------------------------------------------------------------------------------?
# Q=11 Take n from the user and print only the even numbers from 1 to n.
n = int(input("Enter your Number =>"))
i = 2
while i <= n:
    print(i ,end=" ")
    i = i+2


# Q=12 Take n from the user and print only the odd numbers from 1 to n.
n = int(input("Enter your Number =>"))
i = 1
while i <= n:
    print(i ,end=" ")
    i = i+2


# Q=13 Take n from the user and print all numbers from 1 to n that are divisible by 3.
n = int(input("Enter your Number =>"))
i = 3
while i <= n:
    print(i ,end=" ")
    i = i+3


# Q=14 Take n from the user and print all numbers from 1 to n that are divisible by both 2 and 3.
n = int(input("Enter your Number =>"))
i = 6
while i <= n:
    print(i ,end=" ")
    i = i+6


# Q=15 Take n from the user and count how many numbers from 1 to n are even.
n = int(input("Enter your Number =>"))
i = 2
Count = 0
while i <= n:
    print(i)
    Count +=1
    i = i+2
print("The Total Count => ", Count)



# D. Calculation Problems   ------------------------------------------------------------------------------------------------------------?
# Q=16 Take n from the user and calculate:
n = int(input("Enter your Number =>"))
i = 1
Total = 0
while i <= n:
    print(i)
    Total +=i
    i = i+1
print("The Total Count => ", Total)


# Q=17 Take n from the user and calculate the sum of all even numbers from 1 to n.
n = int(input("Enter your Number =>"))
i = 2
Total = 0
while i <= n:
    print(i)
    Total +=i
    i = i+2
print("The Total Count => ", Total)


# Q=18 Take n from the user and calculate the sum of all odd numbers from 1 to n.
n = int(input("Enter your Number =>"))
i = 1
Total = 0
while i <= n:
    print(i)
    Total +=i
    i = i+2
print("The Total Count => ", Total)


# Q=19 Take a number from the user and print its multiplication table from 1 to 10.
n = int(input("Enter your Number =>"))
i = 1
while i <= 10:
    print(f"{n} * {i}  = {n*i}")
    i = i+1


# Q=20 Take a number n and calculate:
n = int(input("Enter your Number =>"))
i = 1
Total = 1
while i <= n:
    print(i)
    Total *=i
    i = i+1
print( "The Total Count => ", Total)




# E. String Iteration  ---------------------------------------------------------------------------------------------------------------------?
# Q=21 Take a string from the user and print each character on a separate line.
string = input("Enter your string =>")
i=0
while i<len(string):
    print(string[i])
    i += 1


# Q=22 Take a string from the user and print all its characters on the same line using end="".
string = input("Enter your string =>")
i=0
while i<len(string):
    print(string[i], end=" ")
    i += 1


# Q=23 Take a string from the user and count the number of characters in it using a for loop.
string = input("Enter your string =>")
i= 0
Count = 0
while i<len(string):
    print(string[i],end=" ")
    Count += 1
    i += 1
print("Total Count => ", Count)
    

# Q=24 Take a string from the user and count how many times the character "a" appears.
string = input("Enter Your string => ")
Count = 0
i = 0
while i< len(string):
    if string[i] == 'a':
        print(string[i])
        Count += 1
    i+= 1
print(" Total count =>",Count)


# Q=25 Take a string from the user and count how many characters are uppercase letters.
string = input("Enter Your string => ")
Count = 0
i = 0
while i< len(string):
    if chr(65)<=string[i]<=chr(90):
        print(string[i])
        Count += 1
    i += 1
print(" Total count =>",Count)




# F. Nested while Loops   ------------------------------------------------------------------------------------------------------------?
# Q=26 Use nested loops to print:
i = 1
while i <= 3:
    j = 1
    while j <= 4:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1


# Q=27 Use nested loops to print:
i = 1
while i <= 4:
    j = 1
    while j <= 5:
        print("*", end="")
        j = j+1
    print()
    i = i+1


# Q=28 Print the following pattern:
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j = j + 1
    print()
    i = i + 1


# Q=29 Print the following pattern:
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1


# Q=30 Create a multiplication-table grid using nested for loops. ? For example, for numbers 1 to 5, produce rows showing their multiplication results.
Number = int(input("Enter Your Number => "))
i = 1
while i <= Number:
    j = 1
    while j <= 10:
        print(f"{i}*{j}={i*j}", end="\t")
        j = j + 1
    print()
    i = i + 1



