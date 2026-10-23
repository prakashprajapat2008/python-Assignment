if 18 <= age <= 60:


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
        4
        j -= 1
    else:
        p = False
        i = j
if p:
    print("string is =>, True")
else:
    print("string is =>, False")


for i in range(1, 11):
    if i == 6:
        break
    print(i)


numbers = [10, 20, 30, 40, 50]
for num in numbers:
    if num == 30:
        print("Found")
        break


num = int(input("Enter Your Number => "))
while num:
    if num == 0:
        break

     
for i in range(1, 100):
    if i%17 == 0:
        break
    print(i)


i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue

    print(i)
    i += 1 

for i in range(2, 8, 2):
    print(i)
    if i == 4:
        break
    print("Hello")
print("After loop")

for i in range(1, 4):
    if i == 2:
        pass
        print("Inside if")
    print("Outside if", i)


for i in range(5):
    pass

x = 10
if x > 5:
    pass
print("Program finished")

for i in range(1, 6):
    if i == 3:
        continue
else:
    print("Loop completed")






for i in range(1,21):
    if i == 20:
        continue
    print(i)


numbers = [10, -2, 30, -5, 40, -8]
for num in numbers:
    if num<0:
        continue
    print(num)

for i in range(1,20):
    if i%3 == 0:
        continue
    print(i)

numbers = [5, 12, 8, 21, 30, 7]
for num in numbers:
    if num<10:
        continue
    print(num)

for i in range(1, 6):
    if i == 3:
        break
    print(i) 


i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    i += 1
  

i = 1

while i <= 5:
    if i == 3:
        continue

    print(i)
    i += 1


for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break

    print(i)


for i in range(1, 6):
    if i == 3:
        break
else:
    print("Done")



while True:
    number = int(input("Enter Your number => "))
    if number == 0:
        break
    if number < 0:
        continue
    print(number)


numbers = [12, 5, -4, 18, 0, 25, 30]
for number in numbers:
    if number < 0:
        continue
    if number == 0:
        break
    print(number)

numbers = [10, 20, 30, 40, 50]
Hint = 60
for number in numbers:
    if number == Hint:
        print("Number found")
        break
else:
    print("Number not found")

for i in range(1, 5):
    if i == 1:
        break
    print(i)

print("End")


for i in range(1, 7):
    print(i)
    if i == 4:
        break
print("Finished")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

for i in range(1, 5):
    if i == 2:
        pass
    print(i)

for i in range(3):
    print("Python")
else:
    print("Done")

for i in range(1, 5):
    print("A", i)
    if i == 3:
        break
    print("B", i)

for i in range(1, 5):
    if i == 2:
        continue
    print("Value:", i)
    print("Next line")

for i in range(1, 4):
    if i == 2:
        pass
        print("Inside if")
    print("Outside if", i)


for i in range(2, 8, 2):
    print(i)
    if i == 4:
        break
    print("Hello")

print("After loop")

for i in range(1, 5):
    print("Start", i)
    if i == 3:
        continue
    print("End", i)

for i in range(2, 5):
    print(i)
else:
    print("Loop completed")

for i in range(1, 6):
    if i == 4:
        break
    print(i)
else:
    print("Completed")
print("Program end")

for i in range(1, 5):
    if i % 2 == 0:
        continue
    print(i)
else:
#     print("Completed")

for i in range(5, 5):
    print(i)
else:
    print("Else executed")


for letter in "CODE":
    print(letter)
    if letter == "D":
        break
else:
    print("All letters checked")

for i in range(1, 4):
    if i == 2:
        pass
    print(i)
else:
    print("Finished normally")

word = "banana"

for ch in word:
    if ch == "n":
        print("Found")
        break
else:
    print("Not found")

word = "apple"

for ch in word:
    if ch == "z":
        print("Found")
        break
else:
    print("Not found")

for ch in "education":
    if ch in "aeiou":
        continue
    print(ch, end="")
print()

for ch in "programming":
    if ch == "g":
        break
    print(ch, end="-")

for ch in "computer":
    if ch == "o":
        continue
    if ch == "t":
        break
    print(ch, end="")

for ch in "cat":
    if ch == "a":
        pass
    print(ch.upper(), end=" ")

n = 1
while n <= 5:
    print(n)
    if n == 3:
        break
    n += 1
print("Stopped")

n = 0

while n < 5:
    n += 1
    if n == 3:
        continue
    print(n)

n = 1

while n <= 5:
    if n == 2:
        n += 1
        continue
    print(n)
    n += 1

n = 1

while n <= 4:
    if n == 3:
        break
    print(n)
    n += 1

print(n)

for row in range(1, 4):
    for col in range(1, 5):
        if col == 3:
            break
        print(row, col)

for row in range(1, 3):
    for col in range(1, 4):
        if col == 2:
            continue
        print(row, col)

for i in range(1, 4):
    print("Outer", i)
    for j in range(1, 4):
        if j == 2:
            break
        print("Inner", j)

for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print(i, j)
    else:
        print("Inner else", i)

for i in range(1, 3):
    for j in range(1, 4):
        if j == 2:
            continue
        print(i, j)
    else:
        print("Inner loop complete")

for i in range(1, 7):
    if i == 2:
        continue
    if i == 5:
        break
    print(i)
else:
    print("Loop else")
print("End")

for i in range(1, 5):
    if i == 3:
        pass
    else:
        print("Else block", i)
    print("Number", i)

for i in range(1, 5):
    print("X", end="")
    if i == 2:
        continue
    print("Y", end="")
print("Z")

for i in range(1, 5):
    if i == 2:
        pass
    elif i == 3:
        continue
    elif i == 4:
        break
    print(i)
else:
    print("Completed")
print("Outside")

string = input("Enter Your string => ")
target = input("Enter target character => ")
for ch in string:
    print(ch, end=" ")
    if ch == target:
        break

Number = int(input("Enter Your Number =>"))
for num in Number:
    if num < 0:
        break
    print(num, end=" ")



numbers = list(map(int, input().split()))

for num in numbers:
    if num < 0:
        break
    print(num, end=" ")

string = input("Enter Your string => ")
target = input("Enter Your target => ")
for word in string.split():
    if word == target:
        print("Found")
        break
else:
    print("Not found")


N = int(input("Enter Your Number => "))
for i in range(1, N + 1):
    if i % 3 == 0:
        continue
    print(i, end=" ")

string = input("Enter Your string => ")
target = input("Enter Your Target => ")
for ch in string:
    if ch == target:
        continue
    print(ch, end="")








def function_name():
    # function_code
function_name()


def add():
    a = 10
    b = 20
    print("The Total Add =>", a + b)
add()


def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
number = int(input("Enter Your Number =>"))
even_or_odd(number)


def print_stars():
    print("    *     ")
    print("   * *   ")
    print("  * * *  ")
    print(" * * * * ")
    print("* * * * *")
print_stars()


def add():
    a = 10
    b = 20
    print("The Total Add =>", a + b)
    print("The Total Add =>", a - b)
    print("The Total Add =>", a * b)
    print("The Total Add =>", a / b)
    print("The Total Add =>", a % b)
    print("The Total Add =>", a ** b)
    print("The Total Add =>", a // b)
add()


def add():
   a = 2
   if a%2 == 0:
      print("Even")
   else:
        print("odd")
add()


greet()
def greet():
    print("Hello")


def stars():
    for i in range(1, 6):
        print(" " * (5 - i) + "* " * i)
stars()


def stars():
    for i in range(1, 6):
        print(" " * (5 - i) + "* " * i)
    for i in range(5, 0, -1):
        print(" " * (5 - i) + "* " * i)
stars()

string = input("Enter Your string => ")
count = 0
for ch in string.lower():
    if ch in "aeiou":
        continue
    count += 1
print("Total Number => ", count)

N = list(map(int ,input("Enter Your Numbers => ").split()))
target = int(input("Enter Your target => "))
for num in N:
    if num == target:
        print("Found")
        break
else:
    print("Not found")

string = input("Enter Your string => ")
target = input("Enter Your character => ")

for ch in string:
    if ch == target:
        print("Character exists")
        break
else:
    print("Character missing")

for x in range(3):
    continue
else:
    print("A")

for x in range(3):
    break
else:
    print("B")

N = list(map(int, input("Enter Your Numbers => ").split()))
target = int(input("Enter Your target = >"))
for num in N:
    if num < 0:
        continue

    if num == target:
        print("Target found")
        break
else:
    print("Target not found")


def even_or_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

number = int(input("Enter Your Number =>"))
even_or_odd(number)


a=5
b=10
c=20
def add(a,b):
    c=a+b
    return c
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
result=sub(add(a,b),c)
print(result)
print(mul(sub(add(a,b),c),a))
print(mul(sub(a,b),add(b,c)))


def double(num):
    return num * 2
def add_five(num):
    return num + 10
result = add_five(double(20))
print(result)

def describe(name, age, city):
    print(name, age, city)

describe("Asha","21", city="Pune")

def show(a, b=5):
    print(a, b)

show(10)
show(10, 20)
show(a=7, b=3)

def total(a, b, c=10):
    return a + b + c

print(total(1, c=3, b=2))

n = int(input("Enter Your Number => "))
for i in range(1, n + 1):
    for j in range(1, n + 2):
        print("*", end="")
    print()

def show_rules():
    print("Best One Classroom Rules.")
    print("Best Two Classroom Rules..")
    print("Best Therr Classroom Rules..")
show_rules()


def show_square():
    print("****")
    print("****")
    print("****")
    print("****")
show_square()


def show_menu():
    print("Prakash")
    print("Prajapat")
    print("Dev")
show_menu()
show_menu()


def morning_message():
    print("Good morning")
def evening_message():
    print("Good evening")
evening_message()
morning_message()

def show_student_card():
    print("Student Card => ")
    print("Student Name => ")
    print("Roll Number => ")
show_student_card()

def print_numbers():
    print(1)
    print(2)
    print(3)
    print(4)
    print(5)
print_numbers()
print_numbers()

def show_pattern():
    print("*")
    print("**")
    print("***")
show_pattern()
show_pattern()

def show_header():
    print("Day Report")
def show_body():
    print("Week End Report")
def show_footer():
    print("End of report")
show_header()
show_body()
show_footer()


def show_separator():
    print("====================")
print("Day Report")
print("Week End Report.")
show_separator()
print("End of report")


def show_table_heading():
    print("Name", "Roll Number", "Grade", sep="\t")
show_table_heading()
print("Prakash Prajapat", "112603", "A", sep="\t")
print("Dev", "102", "B", sep="\t")

def print_stars():
    print("*****")
print_stars()
print_stars()
print_stars()
print_stars()

def show_welcome():
    print("Welcome to Python")
    print("Course => Python Programming")
show_welcome()

def show_help():
    print("Welcome to Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
def add():
    a = 10
    b = 20
    print("The Total Add =>", a + b)
    print("The Total Subtract =>", a - b)
    print("The Total Multiply =>", a * b)
    print("The Total Divide =>", a / b)
    print("The Total Modulus =>", a % b)
    print("The Total Power =>", a ** b)
    print("The Total Floor Division =>", a // b)

show_help()

print("\n----- Calculator Menu -----")
add()

def print_opening():
    print("===== Welcome =====")
def print_closing():
    print("===================")
print_opening()
print("Item: Notebook")
print("Price => Rs. 50")
print_closing()

def print_box():
    print("***********************")
    print("*  Welcome TO Nagaur  *")
    print("***********************")
print_box()
print_box()

def show_title():
    print("===== Kamdhenu Nagaur =====")
def show_menu():
    print("1. Add student")
    print("2. View students")
    print("3. Exit")
def show_closing_message():
    print("--> Thank you Kamdhenu Nagaur All Student")
show_title()
show_menu()
show_closing_message()

def greet(name):
    print("Hello,", name)
greet("Prakash")

def calculate(a, b):
    return a + b, a - b, a * b, a / b
sum, difference, product,quotient = calculate(300, 7)
print("Sum =>", sum)
print("Difference =>", difference)
print("Product =>", product)
print("Quotient =>", quotient)


def count_digits(number):
    if number == 0:
        return 1
    count = 0
    while number > 0:
        count += 1
        number //= 10
    return count
print(count_digits(12345)) 
print(count_digits(0))      


def classify_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
print(classify_number(10))  
print(classify_number(-3)) 
print(classify_number(0))   


def calculate_total(price, quantity=1):
    return price * quantity
print(calculate_total(100))      # 100
print(calculate_total(100, 3))   # 300


def create_email(username, domain="example.com"):
    return f"{username}@{domain}"
print(create_email("PrakashPrajapat"))
print(create_email("DevPrakash.", "gmail.com"))


def format_name(first, last, uppercase=False):
    full_name = first + " " + last
    if uppercase:
        return full_name.upper()
    return full_name
print(format_name("PrakashDev", "Prajapat"))
print(format_name("PrakashDev", "Prajapat", True))


def percentage(marks, total=100):
    return (marks / total) * 100
print(percentage(95))
print(percentage(76, 80))


def convert_minutes(minutes, seconds_per_minute=60):
    return minutes * seconds_per_minute
print(convert_minutes(20))      
print(convert_minutes(10, 60))


def bill(item, quantity=1, price=100):
    return item, quantity * price
print(bill("Phone => ", 1000, 15))
print(bill(item="Laptop => ", quantity=100, price=850))


def calculate_stats(a, b, c):
    small = min(a, b, c)
    largest = max(a, b, c)
    total = a + b + c
    return small, largest, total
print(calculate_stats(5, 20, 25))



def make_sentence(subject, verb, object):
    sentence = subject + " " + verb + " " + object
    return sentence
print(make_sentence(verb = "Dev", object = "Prajapat", subject = "Prakash"))


def apply_discount(price, discount=0):
    final_price = price - (price * discount / 100)
    return final_price
print(apply_discount(1000, 20))
print(apply_discount(500))


def calculate_pay(hours, rate = 200, bonus = 0):
    return hours * rate + bonus
print(calculate_pay(24, bonus = 82, rate = 506))
print(calculate_pay(24, 842, bonus = 506))


def get_coordinates(x = 0, y = 0):
    return x, y
print(get_coordinates())
print(get_coordinates(y = 5))


def compare(a, b):
    if (a > b):
        result = "A is greater => "
    elif b > a:
        result = "B is greater => "
    else:
        result = "Equal"
    diff = a - b
    if diff < 0:
        diff = -diff
    return result, diff
print(compare(10, 5))


def convert_temperature(value, scale="C"):
    if scale == "C":
        return (value * 9/5) + 32
    else:
        return (value - 32) * 5/9
print(convert_temperature(20))
print(convert_temperature(85.6, "F"))


def order_summary(item, quantity=1, price=100, delivery_fee=40):
    total = item, quantity * price + delivery_fee
    return total
print(order_summary("Phone", delivery_fee=15000))


def show_square():
    print("****")
    print("****")
    print("****")
    print("****")
show_square()


def show_help():
    print("Welcome to Simple Calculator")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")
def add():
    a = 10
    b = 20
    print("The Total Add =>", a + b)
    print("The Total Subtract =>", a - b)
    print("The Total Multiply =>", a * b)
    print("The Total Divide =>", a / b)
    print("The Total Modulus =>", a % b)
    print("The Total Power =>", a ** b)
    print("The Total Floor Division =>", a // b)
show_help()
print("\n----- Calculator Menu -----")
add()


def student_report(name, m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3
    if average >= 40:
        status = "Pass"
    else:
        status = "Fail"
    return name, total, average, status
print(student_report("Aman", 70, 80, 90))


def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result
print(power(2, 4))


def print_box():
    print("*****")
    print("*   *")
    print("*****")
print_box()


def result(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"
print(result(65))


def student_result(a, b, c):
    total = a + b + c
    average = total / 3
    return total, average
print(student_result(80, 90, 70))


def squares(numbers):
    result = []
    for n in numbers:
        result.append(n * n)
    return result
print(squares([2, 3, 4]))


def add(*args):
    print(args)
add(10, 20)


def students(*args):
    print(args)
students(("Aman", 18),("Rahul", 19),("Sumit", 18),("Ravi", 20))


def div(a,b,/,*,c,d):
    return a / b, c * d
print(div(10,5, c=15, d=2))
   

def book(st, de="Nagaur", /, *, passenger, seat="regular"):
    print(st, "to", de)
    print("Passenger:", passenger)
    print("Seat:", seat)
book("Gujarat", passenger="Ravinder", seat="window")


def add(*args):
    print(args)
add(10,20,30)



def add(*args):
    print(args)
add()


def add(*args):
    print(args)
add(a=10,b=20,c=30)


def add(a,b,*,c):
    return a,b,c
div = (10,20,30,40)
print(div)


def show_details(*args,**kwargs):
    print(kwargs,args)
    print(type(kwargs))
    print(type(args))
show_details(10,20,30,name="Prakash Prajapat", age=20, city="Nagaur", Father_Name="Kailash Ram Prajapat")







