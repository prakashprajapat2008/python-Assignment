# Q=1 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
if Number%2==0:
    print("Even")
else:
    print("Odd")


# Q=2 -----------------------------------------------------------------------------------------?
N1 = int(input("Enter your Number =>"))
N2 = int(input("Enter your Number =>"))
if N1 > N2:
    print(f"N1 is Big =>{N1}")
else:
    print(f"N2 is Big =>{N2}")


# Q=3 -----------------------------------------------------------------------------------------?
N1 = int(input("Enter your Number =>"))
N2 = int(input("Enter your Number =>"))
N3 = int(input("Enter your Number =>"))
if N1 > N2 and N1 > N3:
    print(f"N1 is Big =>{N1}")
elif N2 > N1 and N2 > N3:
    print(f"N2 is Big =>{N2}")
else:
    print(f"N3 is Big =>{N3}")


# Q=4 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
if Number>0:
    print(f"+ve =>{Number}")
elif Number<0:
    print(f"-ve =>{Number}")
else:
    print(f"Zero =>{Number}")


# Q=5 -----------------------------------------------------------------------------------------?
Age = int(input("Enter your Age =>"))
if Age<=8:
    print("child")
elif Age<=15:
    print("Teenager")
else:
    print("Adult")


# Q=6 -----------------------------------------------------------------------------------------?
Marks = int(input("Enter your Marks =>"))
if Marks>=90 and Marks<=100:
    print("A")
elif Marks>=80 and Marks<=89:
    print("B")
elif Marks>=70 and Marks<=79:
    print("C")
elif Marks>=60 and Marks<=69:
    print("D")
else:
    print("F")


# Q=7 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
if Number%5==0:
    print(f"Number is Divisible by 5 =>{Number}")
else:
    print(f"Number is not divisible by 5 =>{Number}")


# Q=8 -----------------------------------------------------------------------------------------?
Number = int(input("Enter your Number =>"))
if Number%3==0 and Number%5==0:
    print(f"Number is divisible by 3 and 5 =>{Number}")
else:
    print(f"Number is not divisible by both =>{Number}")


# Q=9 -----------------------------------------------------------------------------------------?
Year = int(input("Enter your Year =>"))
if Year%4==0 and Year%400==0:
    print(f"Leap Year =>{Year}")
else:
    print(f"Not a Leap Year =>{Year}")


# Q=10 -----------------------------------------------------------------------------------------?
range = int(input("Enter your Range =>"))
if range>=10 and range<=50:
    print(f"in Range =>{range}")
else:
    print(f"Out of Range =>{range}")







    