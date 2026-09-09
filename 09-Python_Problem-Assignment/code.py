#Level 1 — Intermediate
#1. Positive, Negative, or Zero
#Q=1 ----------------------------------------?
Number = int(input("Enter your Number:"))
if Number>0:
    print("+ve")
elif Number<0:
    print("-ve")
else:
    print("Zero")    


#2. Even or Odd + Positive or Negative
#Q=2 ------------------------------------------?
Number = int(input("Enter your Number:"))
if Number>0 and Number%2==0:
    print("+ve Even")
elif Number>0 and Number%2==1:
    print("+ve Odd")
elif Number<0 and Number%2==0:
    print("-ve Even")
elif Number<0 and Number%2==1:
    print("-ve Odd")
else:
    print("Zero")


#3. Largest of Two Numbers
#Q=3 ---------------------------------------------?
X = int(input("Enter your Number:"))
Y = int(input("Enter your Other Number:"))
if X>Y:
    print(f"The larger Number is X {X}:")
elif X<Y:
    print(f"The larger Number is Y {Y}:")
else:
    print("Both are equal")


#4. Smallest of Three Numbers
#Q=4 ------------------------------------------------?
X = int(input("Enter your Number:"))
Y = int(input("Enter your Others Number:"))
Z = int(input("Enter your More Number:"))
if X<Y and X<Z:
    print(f" X={X}:")
elif X>Y and Y<Z:
    print(f" Y={Y}:")
else:
    print(f" Z={Z}:")


#5. Largest of Three Numbers
#Q=5 -------------------------------------------------?
X = int(input("Enter your Number:"))
Y = int(input("Enter your Others Number:"))
Z = int(input("Enter your More Number:"))
if X>Y and X>Z:
    print(f" X={X}:")
elif X<Y and Y>Z:
    print(f" Y={Y}:")
else:
    print(f" Z={Z}:")


#6. Divisible by 5 and 11
#Q=6 ---------------------------------------------------?
X = int(input("Enter your Number :"))
if X%5==0 and X%11==0:
    print("Divisible by both 5 and 11")
elif X%5==0 and X%11!=0:
    print("Divisible only by 5:")
elif X%5!=0 and X%11==0:
    print("Divisible only by 11")
elif X%5!=0 and X%11!=0:
    print("Divisible by neither")


#7. Divisible by Either 3 or 7
#Q=7 -----------------------------------------------------?
X = int(input("Enter your Number :"))
if X%3==0 and X%7==0:
    print("Divisible by both 3 and 7:")
elif X%3==0 and X%7!=0:
    print("Divisible only by 3:")
elif X%3!=0 and X%7==0:
    print("Divisible only by 7:")
elif X%3!=0 and X%7!=0:
    print("Divisible by neither")


#8. Pass or Fail
#Q=8 -------------------------------------------------------?
marks = int(input("Enter your marks:"))
if marks<0:
    print("Invalid marks1:")
elif marks>100:
    print("Invalid marks2:")
elif marks>=40:
    print("Pass:")
elif marks<40:
    print("Fail:")


#9. Grade Calculator
#Q=9 ----------------------------------------------------------?
marks = int(input("Enter your marks:"))
if marks<0:
    print("Invalid marks1:")
elif marks>100:
    print("Invalid marks2:")
elif marks>=100 or marks>=90:
    print("A:")
elif marks>=89 or marks>=80:
    print("B:")
elif marks>=79 or marks>=70:
    print("C:")
elif marks>=69 or marks>=60:
    print("D:")
elif marks>=59 or marks>=40:
    print("E:")
elif marks<40:
    print("Fail:")


#10. Voting Eligibility
#Q=10 --------------------------------------------------------?
Age = int(input("Enter your Age:"))
if Age<0:
    print("Invalid age:")
elif Age>120:
    print("Invalid age 2:")
elif Age<18:
    print("Cannot vote:")
elif Age>=18:
    print("Can vote:")


#Level 2 — More Logical Conditions
#11. Leap Year
#Q=11 ----------------------------------------------------------?
Year = int(input("Enter your Leap Year or Not Leap Year:"))
if Year%400==0 or Year%4==0 and Year%100!=0:
    print("Leap Year:")
else:
    print("Not Leap Year:")


#12. Character Type
#Q=12 -------------------------------------------------------------?
C = input("Enter your Character :")
if C >= 'A' and C <= 'Z':
    print("Uppercase alphabet:")
elif C >= 'a' and C <= 'z':
    print("Lowercase alphabet:")
elif C >= '0' and C <= '9':
    print("Digit:")
else:
    print("Special character:")


# #13. Vowel or Consonant
# #Q=13 ---------------------------------------------------------------?
# C = input("Enter your character: ")
# if C!= 'a,e,i,o,u':
#     if C!= 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z':
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Invalid input")


#14. Profit or Loss
#Q=14 ---------------------------------------------------------------?
cp = float(input("enter your cost price:"))
sp = float(input("enter your selling price: "))
if sp>cp:
    print("profit",sp-cp)
elif cp>sp:
    print("loss",cp-sp)
else:
    print("No profit and no loss")


#15. Profit/Loss Percentage
#Q=15 -------------------------------------------------------------------?
cost_price=float(input("enter in cost price"))
selling_price=float(input("enter in selling price"))
if selling_price>cost_price:
    profit = selling_price - cost_price
    print( "profit",profit / cost_price * 100)
elif cost_price>selling_price:
    loss = cost_price - selling_price
    print("loss",loss / cost_price * 100)
else:
    print("none")


#16. Electricity Bill
#Q=16 ----------------------------------------------------------------------?
bill=int(input("Enter your Electricity bill :"))
if 0<=bill<=100:
    print("₹5 per unit",bill*5)
elif 100<=bill<=200:
    print("₹7 per unit",bill*7)
else:
    print("₹10 per unit",bill*10)


#17. Simple Calculator
#Q=17 -----------------------------------------------------------------------?
a1= int(input("Enter your first Number:"))
a2= int(input("Enter your secend Number:"))
a3= input("Enter your Operator (+,-,*,/ ):")
if  a3=="+":
    print((a1+a2),"right")
elif a3=="-":
    print((a2-a1),"kamdhenu")
elif a3=="*":
    print((a2*a1),"nagaur")
elif a3=="/":
    print((a1/a2),"dev")
else:
    print("prakash")


#18. Temperature Classifier
#Q=18 -------------------------------------------------------------------------------?
Tem = int(input("Enter your marks:"))
if Tem<0:
    print("freezing")
elif 0<=Tem<=15:
    print("very cold")
elif 16<=Tem<=25:
    print("cold")
elif 26<=Tem<=35:
    print("normal")
else:
    print("Hot")


#19. Number Range Checker
#Q=19 -------------------------------------------------------------------------------------?
marks = int(input("Enter a number: "))
if marks < 0:
    print("Negative")
elif 0<= marks <= 10:
    print("Number is between 0 and 10")
elif 11<= marks <= 50:
    print("Number is between 11 and 50")
elif 51<= marks <= 100:
    print("Number is between 51 and 100")
else:
    print("Above 100")


#20. Triangle Validator
#Q=20 -----------------------------------------------------------------------------------------?
X = float(input("Enter your first side: "))
Y = float(input("Enter your second side: "))
Z = float(input("Enter third side: "))
if X+Y>Z and X+Z>Y and Y+Z>X:
    print("Valid triangle")
else:
    print("Invalid triangle")


#Level 3 — Harder Conditional Problems
#21. Triangle Type
#Q=21 --------------------------------------------------------------------------------------------?
X = int(input("Enter your first side: "))
Y = int(input("Enter your second side: "))
Z = int(input("Enter third side: "))
if X+Y>Z and X+Z>Y and Y+Z>X:
    print("Equilateral:")
elif X+Y>Z and X+Z>Y and Y+Z<X:
    print("Isosceles:")
else:
    print("Scalene:")


#22. ATM Withdrawal
#Q=22 ------------------------------------------------------------------------------------------------?
account_balance=int(input("enter your account balance:"))
withdrawal_amount=int(input("enter your withdrawal amount:"))
if withdrawal_amount>0 and withdrawal_amount%100==0 and account_balance>withdrawal_amount and  withdrawal_amount+500<account_balance:
     print("withdrawl successful")
     print("remaining balance:", account_balance-withdrawal_amount)
else:
     print("none")


#23. Login System
#Q=23 ------------------------------------------------------------------------------------------------?
username=input("Enter your username:")
password=input("Enter your password:")
if username == "admin" and password== "python123":
    print("login successful")
elif username!="admin" and password=="python123" :
    print("user not found")
elif  username=="admin" and password!="python123" :
    print("wrong password")
else:
    print("dono wrong h")


#24. Discount Calculator
#Q=24 ------------------------------------------------------------------------------------------------?
amount=int(input("Enetr your purchase amount:"))
if 0<amount<=500:
    discounta=amount*0
    print("Discount: 0%" "\nDiscount amount:",discounta, "\nFinal amount:",amount-discounta)
elif 500<=amount<=999:
    discounta=(amount*5)/100
    print("Discount: 5%" "\nDiscount amount:",discounta, "\nFinal amount:",amount-discounta)
elif 1000<=amount<=1999:
    discounta=(amount*10)/100
    print("Discount: 10%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)
elif 2000<=amount<=4999:
    discounta=(amount*15)/100
    print("Discount: 15%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)
elif amount>=5000:
    discounta=(amount*20)/100
    print("Discount: 20%" "\nDiscount amount:",discounta ,"\nFinal amount:",amount-discounta)    
else:
    print("please enter valid amount")


#25. Student Result System   
#Q=25 ----------------------------------------------------------------------------------------------?
Git=int(input("Enter your in Git subjects marks:"))
Python=int(input("enter your in Python subjects marks: "))
Github=int(input("enter your in Github subjects marks:"))
if 0<Git<=100 and 0<Python<=100 and 0<Github<=100:
    if Git<35 or Python<35 or Github<35:
        print("Fail")
    else:
        total=Git+Github+Python
        average=total/3
        if average>=75:
            print("Distinction")   
        elif 60<=average<=74 :
            print("First Class")
        elif 50<=average<=59:
            print("Second Class")
        elif 35<=average<=49:
            print("pass")
        else:
            print("not result found")

#26. Date Validator
#Q=26 ------------------------------------------------------------------------------------------------?
Day=int(input("Enter your day:"))
Month=int(input("Enter your month:"))
Year=int(input("Enetr your year:"))
if 0<Day<32 and 0<Month<13 and Year>0:
    if Month==1 or Month==3 or Month==5 or Month==7 or Month==8 or Month==10 or Month==12:
        print("valid")
    elif(Month==4 or Month==6 or Month==9 or Month==11) and Day<31:
        print("valid")
    elif (Month==4 or Month==6 or Month==9 or Month==11) and Day==31:  
        print("date is not valid")  
    else:
        if Month==2 and (Year%400==0 or Year%4==0) and Year%100!=0 and Day==29:  
            print("valid")  
        elif Month==2 and Day<29:
            print("valid")
        else:
            print("date is not valid")    
else:
    print("date is not valid")                     

#27. Time Validator
#Q=27 -------------------------------------------------------------------------------------------------?
hours=int(input("Enter Your in hours:"))
minutes=int(input("Enter Your in minutes:"))
seconds=int(input("Enter Your in seconds:"))
if 0<hours<23:
    if 0<minutes<59:
        if 0<seconds<59:
            print("valid time")
else:
            print("invalid time")


#28. Youngest of Three People
#Q=28 ---------------------------------------------------------------------------------------------------?
Rahul = input("Enter Your in name:")
age1 = int(input("Enter Your in age:"))
Amit = input("Enter Your in name:")
age2 = int(input("Enter Your in age:"))
Jay = input("Enter Your in name:")
age3=int(input("Enter Your in age:"))
if age1<age2 and age1<age3:
    print(f"{Rahul} is the youngest")
elif age2<age1 and age2<age1:
    print(f"{Amit} is the youngest")
elif age3<age2 and age3<age2:
    print(f"{Jay} is the youngest")
else:
    if age1==age2 and age2==age3 and age1!=age3:
        print(f"{Rahul} and {ArithmeticError} same")
    elif age2==age3 and age2!=age3 and age2==age1:
        print(f"{Amit} and {Jay} same")  
    else:
        print("three persion same")      


#29. Second Largest of Three Numbers
#Q=29 ---------------------------------------------------------------------------------------------------?
num1=int(input("Enter Your number 1:"))
num2=int(input("Enter Your number 2:"))
num3=int(input("Enter Your number 3:"))
if num1>num2 and num1>num3:
    if num2>num3:
        print(f"Middle number is {num2}")
    else:
        print(f"Middle number is {num3}")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(f"Middle number is {num1}")  
    else:
        print(f"Middle number is {num3}") 
elif num3>num1 and num3>num2:
    if num1>num2:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}")                     
elif num1==num2==num3:
    print(f"Middle number is {num2}")
else:
    if num1==num2:
        print(f"Middle number is {num2}")
    elif num1==num3:
        print(f"Middle number is {num1}")
    else:
        print(f"Middle number is {num2}") 


#30. Complete Scholarship Decision ⭐
#Q=30 ------------------------------------------------------------------------------------------------?
student_age=int(input("Enter Your student age:"))
marks=int(input("Enter Your student marks:"))
family_income=int(input("Enter Your family income:"))
attendance_percentage=int(input("Enter Your student attendance percentage:"))
if 18<=student_age<=25 and 85<=marks<=100 and 0<=family_income<=30000 and  75<=attendance_percentage<=100:
    print("Scholarship Approved")
elif not 18<=student_age<=25:
    print("Scholarship Rejected \nReason: Student age is not satisfied")
elif not 85<=marks<=100:
    print("Scholarship Rejected \nReason: Marks below 85")
elif not 0<=family_income<=30000:
    print("Scholarship Rejected \nReason: family income more than 30000") 
elif not 75<=attendance_percentage<=100:
    print("Scholarship Rejected \nReason: attendance is less than 75%")      
else:
    print("none")



