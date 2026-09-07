#Practice Problems
#A. Basic if
#Q=1 Write a program that checks whether a number is greater than 10. If it is, print:
is_number = 20
if is_number > 10:
    print("Greater than 10")

#Q=2 Write a program that checks whether a person's age is at least 18. If true, print:
age = 25
if age >= 18:
    print("Adult")

#Q=3 Take a number from the user and print Positive if the number is greater than 0.
is_number = int(input("Enter a number: "))
if is_number > 0:
    print("Positive")

#Q=4 Write an if statement that checks whether:
is_marks = 80
if is_marks >= 40:
    print("Pass")

#Q=5 Take a number from the user and print Zero when the number is equal to 0.
is_number = int(input("Enter a number: "))
if is_number == 0:
    print("Zero")

#B. if-else
#Q=6 Write a program that checks whether a number is positive or not.
is_number = int(input("Enter a number: "))
if is_number > 0:
    print("Positive")
else:
    print("Not positive")

#Q=7 Take a person's age and display:
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

#Q=8 Write a program that checks whether a number is even or odd using %.
is_number = int(input("Enter a number: "))
if is_number % 2 == 0:
    print("Even")
else:
    print("Odd")

#Q=9 Take marks from the user and display Pass if marks are at least 40; otherwise display Fail.
is_marks = int(input("Enter marks: "))
if is_marks >= 40:
    print("Pass")
else:
    print("Fail")

#Q=10 Take two numbers and print which one is greater using if-else.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First number is greater")
else:
    print("Second number is greater")

#C. if-elif-else
#Q=11 Write a program that displays:
marks=90
if marks==90:
    print("a")
elif 75<marks<89:
    print("b")
elif 60<marks<74:
    print("c")
elif 40<marks<59:
    print("d")
else:
    print("f")

#Q=12 Take a number from the user and display:
is_number = int(input("Enter a number: "))
if is_number > 0:
    print("Positive")
elif is_number<0:
    print("negative")
else:
    print("zero")

#Q=13 Take a number representing a day:
week_day= int(input("4 monday, 2 tuesday, 6 wednesday, 5 thursday, 8 friday"))
if week_day ==4:
    print("m") 
elif week_day ==2:
    print("t")
elif week_day ==6:
    print("w")
elif week_day ==5:
    print("th")
else:
    print("f")

#Q=14 Take a student's marks and display:
marks = int(input("Enter your marks"))
if marks >= 75:
    print("Excellent")
elif marks >= 60:
    print("Good")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")

#Q=15 Take a number and display whether it is:
number= int(input("Enter your number"))
if number==0:
    print("1")
elif number==1:
    print("2")
else:
    print("3")

#D. Nested Conditions
#Q=16 Write a program that first checks whether a person is at least 18. If yes, check whether the person is at most 60.
age=int(input("Enter your age:")) 
if age>=20:
    if age<=60:
        print("Age Between 18 and 60")
    else:
        print("true")        
else:
    print("none")      

#Q=17 Take marks from the user.?First check whether the student passed (marks >= 40).?If the student passed, check whether marks are at least 75.
marks=int(input("Enter your marks:"))      
if marks>=40:
    if marks>=85:
        print("Good")
    else:
        print("Passed")
else:
    print("Failed")

#Q=18 Write a nested condition that checks whether a number is positive. If it is positive, check whether it is greater than 100.
number= int(input("Entey your number:"))
if number>=0:
    if number>100:
        print(">100")
    else:
        print("<100")
else:
    print("negative")

#Q=19 Take an age.?First check whether the age is at least 18.?If yes, check whether it is at least 60.?Display an appropriate message for each case.
age=int(input("Enter your age:")) 
if age>=20:
    if age<=60:
        print("Age Between 18 and 60")
    else:
        print(">60")        
else:
    print("none") 

#Q=20 Write a nested condition that checks whether a number is non-zero and then checks whether it is positive or negative.
number=int(input("enter your Number:"))
if number!=0:
    if number>0:
        print("Positive")
    else:
        print("Negative")          
else:
    print("Zero")   

#Q=21 Take age and marks from the user.?Print Eligible only when:
age=int(input("Enter your age:"))
marks=int(input("Enter your marks:"))      
if age>=18:
    if marks>=40:
        print("Eligible")
    else:
        print("Not Eligible and >18")
else: 
    print("Not Eligible")            

#Q=22 Take a number and print Special if:
num=int(input("Enter number:"))  
if num<10:
    print("<10")
elif num>100:
    print(">100")
else:
    print("number is <10 nad >100")

#Q=23 Take a user's age and Boolean variable has_id.?Print Allowed only when:
age= int(input("Enter your age:"))
has_id= bool(input("Enter your has_id and boolean:"))
if age >= 18:
    if has_id=="True":
        print("Allowed")
else:
    print("False")

#Q=24 Take two numbers and check whether:
first_number= int(input("Enter your first_number:"))
second_number= int(input("Enter your second_number:"))
if first_number>10:
    if second_number>10:
        print(">10")
    else:
        print("first_number is >10 but second_number is <10")
elif first_number<=10:
    if second_number>10:
        print("second_number is >10 but first_number is <10")
    elif second_number<=10:
        print("<10")

#Q=25 Take a number and check whether it is either:
number=int(input("Enter number:"))
if number<=0:
    if number==0:
        print("Number right 0")
    else:
        print("Number is <0")    
elif number>=100:
    if number==100:
        print("Number right 100")
    else:
        print("Number is >100")            
else:
    print("Number is 1 to 99")

#F. Combining Conditions with Logical Operators
#Q=26 Write a program using not that prints Open when:
is_closed=False
if not is_closed:
    print("Open")

#Q=27 Take a number and check whether it is between 10 and 50 using and.
number=int(input("Enter your number:"))
if number>=10 and number<=50:
    print("Number is between 10 and 50")
else:
    print("Other number")

#Q=28 Take a number and check whether it is outside the range 10 to 50 using or.
number=int(input("Enter number:"))
if number<=10 or number>=50:
    print("Number is Outside 10 and 50")
else:
    print("Number is between 10 and 50") 

#Q=29 Create a program with three Boolean values:
is_student=True
has_id=True
has_ticket=True
if is_student and has_id and has_ticket:
    print("Allowed")
else:
    print("Not allowed")    

#Q=30 Create a small Eligibility Checker program.
age=int(input("Enter your age:"))
marks=int(input("Enter your marks"))
has_id=True
if age>=18 and marks>=40 and has_id:
    print("Eligible")
else:
    print("Not eligible")    







