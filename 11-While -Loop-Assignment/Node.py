# Nested while Loops – Basic Python Problems-----------------------------------------------------------------?
# Q=1 Print a 3×3 Star Grid
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=2 Print Numbers in Rows
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=3 Print Row Numbers
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=4 Increasing Star Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=5 Decreasing Star Pattern
i = 1
while i <= 5:
    j = 1
    while j <= 6-i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=6 Increasing Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=7 Repeated Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=8 Multiplication Tables from 1 to 5
i = 1
while i <= 5:
    j = 1
    while j <= 10:
        print(f"{i}*{j}={i*j}", end="\t")
        j = j + 1
    print()
    i = i + 1


# Q=9 Multiplication Grid
i=1
while i<=3:
    j=1
    while j<=5:
        print(i*j,end=" ")
        j+=1
    print()  
    i+=1  


# Q=10 Print Squares in Rows
i=1
while i<=5:
    j=1
    while j<=5:
        print(j**2,end=" ")
        j+=1
    print()  
    i+=1  


# Q=11 Alphabet Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(chr(j+64), end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=12 Repeated Alphabet Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(chr(i+64), end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=13 Odd Number Pattern
i = 0
while i <= 4:
    j = 0
    while j <= i:
        print((j*2)+1, end=" ")
        j = j + 1
    print()
    i = i + 1



# Q=14 Even Number Pattern
i = 0
while i <= 4:
    j = 0
    while j <= i:
        print((j*2)+2, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=15  5×5 Star Square
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=16  5×5 Number Square
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(j, end=" ")
        j = j + 1
    print()
    i = i + 1


# Q=17 Row-wise Numbers
A = 1
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(A, end=" ")
        j = j + 1
        A += 1
    print()
    i = i + 1


# Q=18 Print 1 to 20 in 4 Rows
A = 1
i = 1
while i <= 4:
    j = 1
    while j <= 5:
        print(A, end=" ")
        j = j + 1
        A += 1
    print()
    i = i + 1


# Q=19 Print Coordinate Pairs
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j = j+1
    print()
    i = i + 1 


# Q=20 Print All Number Combinations
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(i,j)
        j = j + 1
    i = i + 1


# Q=21 10×10 Multiplication Grid
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i}*{j}={i*j}" , end="\t")
        j = j+1
    print()
    i = i + 1 


# Q=22 Repeated Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    print()
    i = i + 1


# Q=23 Decreasing Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= 6-i:
        print(j, end="")
        j = j + 1
    print()
    i = i + 1


# Q=24 Reverse Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= 6-i:
        print(6-j, end="")
        j = j + 1
    print()
    i = i + 1


# Q=25 Repeated Row Number Pattern
i = 1
while i <= 5:
    j = 1
    while j <= 5:
        print(i, end="")
        j = j + 1
    print()
    i = i + 1







