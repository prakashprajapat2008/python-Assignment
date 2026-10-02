# Problem 1
#Take two numbers and print their sum.------?
# INPUT
#     First number
#     Second number
# PROCESSING
#     Add first number and second number
# OUTPUT
#     Sum_value

# 1. Start
# 2. Read first number
# 3. Read second number
# 4. Add the two numbers
# 5. Store the result
# 6. Display the result
# 7. Stop

# input: = 65
# input: = 55
# result: = add
# output: = 120

a = int(input())
b = int(input())
sum_value = a + b
print(sum_value)



# Problem 2
#Take a number and print whether it is even or odd.-----?
# INPUT:
# Number
# PROCESSING
# check number%2==0 and  number%2==1
# output
# even or odd

# start
# read in number
# number%2 in Even
# number%2! in odd
# store the result
# display in result
# stop

# input: = 20
# if input%2==0
# elif input%2==1
# result: = even and odd
# output: = even and odd

number=int(input("Enter Your numbbers:"))
if number%2==0:
    print("even")
else:
    print("odd")



# Problem 3
# Take three numbers and print the largest number.----?
# INPUT:
# first number 
# second number
# three number
# PROCEESING:
#         F>S AND F>T and 
# compare numbers
# OUTPUT:
#       largest number

# Start.
# Input F, S, T.
# Compare all three.
# Print the largest.
# Stop.

# F= 12
# S = 25
# T = 18
# Largest = 25

first_number= int(input("Enter Your first number: "))
second_number = int(input("Enter Your second number: "))
Third_number = int(input("Enter Your third number: "))
if first_number >= second_number and first_number >= Third_number:
    print("Largest =", first_number)
elif second_number >= first_number and second_number >= Third_number:
    print("Largest =", second_number)
else:
    print("Largest =", Third_number)



# Problem 4
# Take a person's age and print whether they are eligible to vote. Assume the minimum age is 18.----?
# input
# Age
# Process	
#       Check if age ≥ 18
# Output
#      Eligible or Not Eligible

# Start.
# Input age.
# If age is at least 18, print Eligible.
# Otherwise print Not Eligible.
# Stop.

# Age = 20
# Output: Eligible to vote

age = int(input("Enter Your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")



# Problem 5
# Take the price of an item. Give a 20% discount when the price is greater than or equal to 2000. Print the final price.----?
# Input
# Price
# Process
#       Apply 20% discount if price ≥ 2000
# Output
#      Final Price

# Start.
# Input price.
# If price is at least 2000:
# Discount = 20%.
# Final price = price − discount.
# Otherwise final price = price.
# Print final price.
# Stop.

# Price = 2500
# Discount = 500
# Final Price = 2000

price = float(input("Enter Your price: "))
if price >= 2000:
    price = price - (price * 20 / 100)
print("Final Price =", price)
	

# Problem 6
# Take three subject marks and calculate the average. Print Pass if the average is at least 40; otherwise print Fail.------?
# Input
# Three subject marks
# Process
#        Calculate average
# Output
#       Pass or Fail

# Start.
# Input three marks.
# Calculate average.
# If average is at least 40, print Pass.
# Otherwise print Fail.
# Stop.

# Marks
# 60
# 50
# 40
# Average = (60+50+40)/3 = 50
# Output: Pass

m1 = float(input("Enter marks of Subject m1: "))
m2 = float(input("Enter marks of Subject m2: "))
m3 = float(input("Enter marks of Subject m3: "))
average = (m1 + m2 + m3) / 3
print("Average =", average)
if average >= 40:
    print("Pass")
else:
    print("Fail") 

