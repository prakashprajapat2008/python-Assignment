print("Hello, python!!")
name="prakash"
age=18
Age="18"
height = 5.8
print(age,Age,height)
print(type(age))
print(type(height))
print(type(name))
print(type(name))
age = 10
height = 10.5
Age = "10"
d = True
e = None
print(type(age))
print(type(height))
print(type(Age))
print(type(d))
print(type(e))

print(2**4//2*3)
print(4//2*3)

a = 10
b = 5
print(a + b)
print(10 + 5.5)
print(2.5 + 3.5)

first_name = "John"
last_name = "Smith"
print(first_name + " " + last_name)

print("Age: " + str(18))

print(10.5 - 2.5)
print(16//3)
print(-10//3)
print(-10%3)

a="prakash"
b="prajapat"
print(b[7])
print(b[-5])

a="prakash"
print(a[:4])
print(a[:8])
print(a[-5:7])
print(a[-7:7])
print(a[-2:-5])
print(a[::-1])
print(a[-5:-2])

First_Name = "prakash"
Last_Name = "kailash"
full_name = First_Name + " " + Last_Name
print(full_name)

word = "Python"
word = "J" + word[1:]
print(word)
word = "J" + word[4:1]
print(word)

name = "python"
print(name.upper())

name = "PYTHON"
print(name.lower())

text = "pYTHON PROGRAMMING"
print(text.capitalize())

text = "python programming language"
print(text.title())

text = "Python"
print(text.swapcase())

text = "HELLO"
print(text.casefold())

message = "Hello Python"
print("Python" in message)
print("Java" in message)

message = "Hello Python"
print("Java" not in message)

text = "Hello Python"
print(text.find("Python"))
print(text.find("Java"))

text = "Hello Python"
print(text.index("Python"))

text = "hello hello"
print(text.count("hello"))

word = "Programming"
print(word[1:8:2])

text = "Python"
print(text[::2])
print(text[1::2])
print(text[::-1])
print(text[3:6])
print(text[5:])

a = "prakash"
print(a.startswith("pr"))
print(a.endswith("sh"))

a = "i like dev"
new_a = a.replace("dev", "prakash")
print(new_a)

a = "papaya papaya papaya"
print(a.replace("papaya", "apple"))

a = "papaya papaya papaya"
print(a.replace("papaya", "apple", 1))

a = "prakash"
print("prakash" in a)
print("pRakash" in a)
print("pRakash" in a.lower())

a = "aa"
print(a==a)
print(a!=a)

a = "5"
b = "5"
print(a<=b)
print(a>=b)
print(a<b)
print(a>b)

a = "aB"
b = "Ab"
print("aB" > "Ab")

a = "aB"
b = "ab"
print("aB" > "ab")

a,b=map(int,input("Enter two numbers: ").split())
print(a,b)
print(a,b, type(a), type(b))

first_name, last_name = input("Enter your first name and last name: ").split()
print( "first name :", first_name, "last name :", last_name)

name = input("Enter student name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))
city = input("Enter city: ")

print("\n--- Student Information ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height:.2f}")
print(f"City: {city}")

a=(input("Enter a birth date: "))
b=(input("Enter a birth month: "))
c=(input("Enter a birth year: "))
print("Birth date is: ", a, b, c,sep="/")

number=int(input("Enter a number: "))
if number%2==0:
    print("Even number")

if number%2==1:
    print("Odd number")

is_indian_army=input("are you indian army ? Yes or No:")
if is_indian_army=="yes":
    age= input("Enter you age:")
    if age>="18":
        print("you're allowed to form:")
    if age<="18":
        print("you're noy allowed to form:")
if is_indian_army=="no":
    print("you're not allowed to form:")

is_indian_army=input("are you indian army ? Yes or No:")
if is_indian_army=="no":
    age= input("Enter you age:")

else :
    print("Enter you not age:")

a1= int(input("Enter your first letter:"))
a2= int(input("Enter your secend letter:"))
number= int(input("Enter your number:"))
if number ==10:
    print((a1+a2),"right")
elif number==12:
    print((a2-a1),"kam")
elif number==100:
    print((a2*a1),"nagaur")
elif number==200:
    print((a1/a2),"mjmj")
else:
    print("prakash")

number = int(input("Enter your Table number:"))
for i in range(1,11):
    print(3*i)

Name = input("Enter Your a staring:").strip().lower()   
length = len(Name)
sum = ""
for Number in range(length-1,-1,-1):
    sum = sum + Name[Number]
    print(sum)

Name = input("Enter Your a staring:").strip().lower()   
length = len(Name)
sum = ""
for Number in range(length-1,-1,-1):
    sum = sum + Name[Number]
print(sum)

Name = input("Enter Your a staring:").strip().lower()   
length = len(Name)
sum = ""
for Number in range(length-1,-1,-1):
    sum = sum + Name[Number]
if Name==sum:
    print("yes")
else:
    print("no")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

num = int(input("Enter number: "))
square = num * num
print("Square:", square)

num = int(input("Enter number: "))
cube = num * num * num
print("Cube:", cube)

marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 40:
    print("Grade D")
else:
    print("Fail")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

amount = float(input("Enter purchase amount: "))
if amount < 500:
    discount = 0
elif amount < 1000:
    discount = 5
elif amount < 2000:
    discount = 10
else:
    discount = 20
discount_amount = amount * discount / 100
final_amount = amount - discount_amount
print("Discount:", discount_amount)
print("Final Amount:", final_amount)





