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

x = input("Enter your string:")
print(x[::-1])

n = input("Enter your number:")
for i in range(2, n+1, 2):
    print(i)

for i in range(2, 21, 2):
    print(i)

n = int(input("Enter your Number:"))
total = 0
for i in range(1, n+1):
    total += i
print(total)

n = int(input("Enter your Number:"))
count = 0
for i in range(1,n+1):
    count = count+i
print("Total Number is Sum count:", count)

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == j-1:
            print('*', end='')
        else:
            print(' ', end='')
print()

n = 5
for i in range(1, n+1):
    print(''*(n-i)+'*'*(2*i-1))
for i in range(n-1, 0, -1):
    print(''*(n-i)+'*'*(2*i-1))

n = 5
for i in range(1, n+1):
    print('* ' * i)
for i in range(n-1, 0, -1):
    print('* ' * i)

for row in range(4):
    for column in range(4):
        print("*", end="")
    print()

for row in range(4):
    print("*"*4)

n = 4
for i in range(1, 5):
    print(''*(i)+'*'*(1*i))
print("")

for row in range(4):
    for column in range(row+1):
        print("*", end="")
    print()

for i in range(7, 71, 7):
    print(i)

for row in range(10):
    for column in range(8):
        print((row+1)*(column+1), end="\t")
    print()

for i in range(1,5):
    for j in range(i,5):
        print("*", end=" ")
    print()

for i in range(1,6):
    for j in range(1,6-i):
        print(" ", end="")
    for i in range(1,i+1):
        print("*", end="")
    print("")

for i in range(6, 0, -1):
    for j in range(6 - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()


for i in range(1, 5):
    for j in range(5 - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")
    print()

for i in range(4, 0, -1):
    for j in range(4 - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("* ", end="")
    print()

for i in range(5):
    for j in range(5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, 6):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == 5:
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1, 4):
    print(" " * (3 - i) + "*" * (2 * i - 1))
for i in range(2, 0, -1):
    print(" " * (3 - i) + "*" * (2 * i - 1))

n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 3
for i in range(1, n + 1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(n - 1, 0, -1):
    for j in range(1, 2 * n):
        if j == n - i + 1 or j == n + i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5
for i in range(n):
    for j in range(2 * n - 1):
        if i == 0 or j == i or j == 2 * n - 2 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * i)
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * i)

rows = 4
cols = 7
for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()



total = 0
Pass = True
grade = ""
for i in range(6):
    marks = int(input("Enter Your Marks;"))
    total+=marks
    if marks>35:
        Pass = False
    if Pass:
        percentage = total/5
    elif Pass>=90:
        print("A+")
    elif Pass>=81:
        print("A")
    elif Pass>=70:
        print("B")
    elif Pass>=60:
        print("C")
    elif Pass>=50:
        print("D")
    else:
        print("E")    
if Pass ==True:
    print(total,percentage,grade)
    print("Pass")
else:
    print("Fail")



        
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

for i in range(6):
    for j in range(i):
        print("*", end="")
    print()    

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print("  ", end="")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print("", end="")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

n = 5
for i in range(n, 0,-1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


n = 3
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1)) 


n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1
            or j == 0 or j == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()


n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


n = 3
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))


n = 4
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)


Number = int(input("Enter Your Number:"))
if Number>0:
    if Number**2:
        print("+ve")
elif Number<0:
    print("Number",("-ve"))
else:
    print("Number",("Errer"))


n = 5
for i in range(n):
    for j in range(n):
        if (i == 0 or i == n - 1
            or j == 0 or j == n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

for i in range(1,6):
    for j in range(2):
        print("*       ", end="")
    print()
for i in range(5):
    print("* ", end="")
print()

for i in range(4):
    for j in range(2):
        print("*      ",end=" ")
    print()
for i in range(5):
    print("* ",end="")
print()


i = 2
while i<=20:
    print(i)
    i +=2


i = 1
while i<=20:
    if i%2==0:
        print(i)
    



str = input("Enter your string => ")
rstr =""
i = len(str) - 1
while i >= 0:
    rstr = rstr + str[i]
    i = i-1
if str == rstr:
    print("string is True")
else:
    print("string is False")



i = 1
while i<=5:
    j = 1
    while j<=i:
        print(i, end="")
        j = j+1
    print()
    i +=1






i=1
while i<6:
    j=1
    while j<i+1:
        print(j,end="")
        j+=1
    k=1
    while k<11-i*2:
        if i<5:
            print(" ",end="")  
        k+=1
    p=1     
    while p<i+1:
        print(i-p+1,end="")
        p+=1 
    i+=1
    print()


i=1
while i<6:
    print(" "*(5-i),end="")
    j=1
    while j<i+1:
        print(j,end="")
        j+=1
    k=1
    while k<i:
        print(i-k,end="")  
        k+=1      
    i+=1
    print()
i=1
while i<5:
    print(" "*(i),end="")
    j=1
    while j<5-i+1:
        print(j,end="")
        j+=1
    k=1
    while k<5-i:
        print(5-k-i,end="")  
        k+=1      
    i+=1
    print()


i=1
while i<6:
    j=1
    while j<i+1:
        print(j,end="")
        j+=1
    k=1
    while k<i:
        if i>1:
            print(i-k,end="")   
        k+=1     
    i+=1
    print()

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i+=1
i = i - 2
while i >= 1:
    j = 1
    while j <= i:
        print(j, end="")
        j = j + 1
    print()
    i-=1



i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    print()
    i+=1
i = i - 2
while i >= 1:
    j = 1
    while j <= i:
        print(i, end="")
        j = j + 1
    print()
    i-=1


string2 = input("Enter Your String =>")
i = 0
j = len(string2)-1
p = True
while i<j:
    if string2[i] == string2[j]:
        i += 1
        j -= 1
    else:
        p = False
        i = j
if p:
    print("string is =>, True")
else:
    print("string is =>, False")


N = int(input("Enter Your Number =>"))
while N > 0:
    digit = N % 10
    print(digit, end="  ")
    N = N // 10

number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print("Reverse:", reverse)

i = 1

while i <= 5:
    print(i)
    i+=1

row = 1
while row <= 3:
    column = 1
    print("*", end=" ")
    while column <= 4:
        print("*", end="")
        column = column + 1

    print()
    row = row + 1

Str = input("Enter Your Str =>")
Str1 = ""
for chr in Str:
    if chr in "0123456789":
        Str1 = Str1+""
    else:
        Str1 = Str1 + chr
print(Str1)


String = input("Enter Your String =>")
C = 0
for i in String:
    if chr(97) <= i <= chr(122):
        print(i, end="")
        C+=1
    print(" The Tota Lowercase Count", C)


Number = input("Enter Your Number =>")
C = 0
for i in Number:
    if Number:
        print(i, end="")
        C = C + 1
    print(" The Tota Lowercase Count", C)


Number1 = int(input("Enter Your Number1 =>"))
Number2 = int(input("Enter Your Number2 =>"))
Choice = int(input("Enter Your Choice => 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Modulus =>"))
match Choice:
    case 1:
        print(Number1 + Number2)
    case 2:
        print(Number1 - Number2)
    case 3:
        print(Number1 * Number2)
    case 4:
        print(Number1 / Number2)
    case _:
        print(Number1 % Number2)


Number1 = int(input("Enter Your Number1 =>"))
Number2 = int(input("Enter Your Number2 =>"))
Choice = int(input("Enter Your Choice => 1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Modulus 6.Exit =>"))
while Choice != 6:
    match Choice:
        case 1:
            print(Number1 + Number2)
        case 2:
            print(Number1 - Number2)
        case 3:
            print(Number1 * Number2)
        case 4:
            print(Number1 / Number2)
        case _:
            print(Number1 % Number2)
    print()
    Choice+=1

n = int(input("Enter your Number =>"))
match True:
    case 1:
        if n% 2==0:
            print("Even Number")
        else:
            print("Odd Number")
    case 2:
        for i in range(2, n):
            if n % i == 0:
                print("Prime Number")
            else:
                print("Not Prime Number")
    case _:
        print("Invalid Number")


n = 5
for i in range(n, 0, -1):
    print("* " * i)


day = 8
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")


marks = int(input("Enter Your Marks =>"))
match marks:
    case marks if marks >= 100:
        print("A")
    case marks if marks >= 90:
        print("B")
    case marks if marks >= 80:
        print("C")
    case marks if marks >= 70:
        print("D")
    case _:
        print("Fail")


gas = input("Enter Your Gas => ")
match gas:
    case "I gas":
        Type = input("Enter booking Type => ")
        match Type:
            case "online":
                print("I online booking")
            case "phone":
                print("I phone booking")
            case _:
                print("Invalid Type")

    case "B gas":
        Type = input("Enter booking Type => ")
        match Type:
            case "online":
                print("B online booking")
            case "phone":
                print("B phone booking")
            case _:
                print("Invalid Type")

    case "hp gas":
        Type = input("Enter booking Type => ")
        match Type:
            case "online":
                print("HP Gas online booking")
            case "phone":
                print("HP Gas phone booking")
            case _:
                print("Invalid Type")

    case _:
        print("Invalid gas company")



day = int(input("Enter day: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case _:
        print("Weekend or Invalid")

choice = 2

match choice:
    case 1:
        print("First")
        print("Option")
    case 2:
        print("Second")
        print("Option")
    case _:
        print("Invalid")


is_user=input("Is user have connection of lpg>>>YES/NO").lower().strip()
match is_user:
    case "yes":
        print("user have connection exist:---")
        can_refill=input("Is user can need refill>>>YES/NO").lower().strip()
        match can_refill:
            case "yes":
                print("user wnat to refill the gas---")
                user_number=int(input("enter your resiteerd mobile number"))
                otp=int(input("enter the sended otp on massage"))
                stored_number=1234567890
                match user_number:
                    case user_number if user_number==stored_number and otp==1234:
                        print("Booking in progress ")
                        is_confirm=input("can want to confirm the booking >>>yes/no").lower().strip()
                        match is_confirm:
                            case x if x=="yes":
                                print("Booking confirmed succesfully!!!!!!!")
                                payment_method=int(input("enter your payment mathod\n1=online\n2=case\n>>>>"))
                                match payment_method:
                                    case 1 | 2:
                                        print("Payment succesfully:")
                                        is_delivery=int(input("enter is the delivory or not \n1=deliveryed\n2=not delivred\n>>>"))
                                        match is_delivery:
                                            case 1:
                                                print("Succesfully delivered to user:")
                                                rating=int(input("enter teh rating regard to delivery\n5=better\n4=best\n3=good\n2=need improvment\n1=wrost"))
                                                match rating:
                                                    case 5:
                                                        print("better")
                                                    case 4:
                                                        print("best")
                                                    case 3:
                                                        print("good")
                                                    case 2:
                                                        print("need improvment")
                                                    case 1:
                                                        print("wrost")
                                                    case _:
                                                        print("Invalid input")
                                            case 2:
                                                print("not delivered to user:")
                                    case _:
                                        print("invalid choice")
                                        

                            case x if x=="no":
                                print("Booking are cancled by user..")
                            case _:
                                print("invalid input")


number = 0

match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")


number = -5
match number:
    case x if x > 0:
        print("Positive")
    case x if x < 0:
        print("Negative")
    case 0:
        print("Zero")


marks = 55
match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case x if x >= 40:
        print("D")
    case _:
        print("Fail")



marks = 85
match marks:
    case x if x >= 90:
        print("A")
    case x if x >= 75:
        print("B")
    case x if x >= 60:
        print("C")
    case _:
        print("Fail")



command = "pause"
choice = 2
match command:
    case "start":
        print("Starting")

    case "pause":
        match choice:
            case 1:
                print("Pause Music")
            case 2:
                print("Pause Video")
            case _:
                print("Invalid Pause Choice")

    case "stop":
        print("Stopping")

    case _:
        print("Unknown Command")



day = 6
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Working Day")
    case 6 | 7:
        print("Holiday")
    case _:
        print("Invalid Day")



choice = 3
age = 17
match choice:
    case 1:
        if age >= 18:
            print("Adult")
        else:
            print("Minor")

    case 2:
        print("Option 2")

    case 3:
        if age >= 18:
            print("Allowed")
        else:
            print("Not Allowed")

    case _:
        print("Invalid")


for i in range(6):
    for j in range(7):
        if (i == 0 and j%3 !=0) or (i == 1 and j%3==0) or (i-j == 2) or (i+j == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



str = input("Enter Your String =>").strip().lower()
i = 0
p = True
for chr in str:
    if chr == "o":
        print("Found")
        i+=1
        break
else:
    print("Not Found")



str = input("Enter Your String =>").strip().lower()
p = True
T = 0
for i in range(0,len(str)):
    T = T+1
    if str[i] == "o":
        p = False
        print("Found")
        break
print(T)
if p:
    print("Not Found")

string = "abcd"
r = string[-1]  
for i in range(len(string) - 1):
    r += string[i]
print(r) 


string2 = input("Enter Your String =>")
i = 0
j = len(string2)-1
p = True
while i<j:
    if string2[i] == string2[j]:
        i += 1
        j -= 1
    else:
        p = False
        i = j
if p:
    print("string is =>, True")
else:
    print("string is =>, False")

