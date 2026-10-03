# Q=11 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1,Number+1):
    print(i, end=" ")
print()


# Q=12 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1,Number+1):
    print(i, end=" ")
print()


# Q=13 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1,Number+1):
    if i%2==0:
        print(i, end=" ")
print()


# Q=14 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1,Number+1):
    if i%2==1:
        print(i, end=" ")
print()


# Q=15 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
count = 0
for i in range(1,Number+1):
    count = count+i
print("Total Number is Sum count:", count)


# Q=16 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
count = 1
for i in range(1,Number+1):
    count = count*i
print("Total Number is product count:", count)


# Q=17 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1, 11):
    print(Number * i, end=" ")
print()


# Q=18 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
count = 0
for i in range(1,Number+1):
    if i%3==0:
        print(i, end=" ")
        count += 1
print()
print("Total numbers divisible by 3:", count)


# Q=19 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
factorial = 1
for i in range(1, Number + 1):
    factorial *= i
print(factorial)


# Q=20 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
for i in range(1, Number + 1):
    print(7 * i, end=" ")
print()
