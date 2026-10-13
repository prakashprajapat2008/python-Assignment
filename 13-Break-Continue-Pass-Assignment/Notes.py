# Q=1 -----------------------------------------------------------------?
for i in range(1, 11):
    if i == 6:
        break
    print(i)


# Q=2 ---------------------------------------------------------------?
numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 30:
        print("Found")
        break


# Q=3 ------------------------------------------------------------------?
num = int(input("Enter Your Number => "))
while num:
    if num == 0:
        break


# Q=4 ------------------------------------------------------------?
for i in range(1, 100):
    if i%17 == 0:
        break
    print(i)


#Q=5------------------------------------------------------------?
i=1
while True:
    num=int(input("enter in numbers:-"))
    if num==0:
        break
    if num<0:
        continue
    print(num)


#Q=6 -------------------------------------------------------------?
numbers = [12, 5, -4, 18, 0, 25, 30]
for i in numbers:
    if i==0:
        break
    if i<0:
        continue
    print(i)


#Q=7--------------------------------------------------------------?
numbers = [12, 5, -4, 18, 0, 25, 30]
for i in numbers:
    if i==0:
        print("Number found")
        break
    else:
        print("Number not Found")
    

        