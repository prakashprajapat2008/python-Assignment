#Practice Problems
#A. Boolean Values
#Q=1 What are the two Boolean values in Python?
A = True
B =False
print(A,B)

#Q=2 What is the data type of:
A = True
print(type(A))

#Q=3 What is the data type of:
A = False
print(type(A))

#Q=4 What is the data type of:
A = True
B = "True"
print(type(A and B))

#Q=5 Why is this:
A = True
print(type(A))

#B. Comparison Operators
#Q=6 What is the result of:
A = 10==10
print(A)

#Q=7 What is the result of:
A = 10 != 5
print(A)

#8 What is the result of:
A = 5 > 10
print(A)

#Q=9 What is the result of:
A = 5 < 10
print(A)

#Q=10 What is the result of:
A = 18 >= 18
print(A)

#Q=11 What is the result of:
A = 18 <= 10
print(A)

#Q=12 Explain the difference between:
name = "prakash"
A = 10 == 10
print(name)
print(A)

#Q=13 Write one example of each comparison operator:
A = 10 == 10    
B = 10 != 5    
C = 10 > 5      
D = 5 < 10      
E = 10 >= 10   
F = 5 <= 10   
print(A)
print(B)
print(C)
print(E)
print(F)

#C. Boolean Expressions
#Q=14 Which of the following are Boolean expressions?
A = 10 + 5
B = 10 > 5
C = "Python"
D = 10 == 20
print(A)
print(B)
print(C)
print(D)

#Q=15 Explain your answer.
age = 20
print(age >= 18)

#Q=16 What is the result?
marks = 45
print(marks == 50)

#Q=17 Create a variable called age and write a Boolean expression that checks whether the age is at least 18.
age = 20
print(age >= 18)

#D. Logical Operators
#Q=18 Find the result of each:
A = True and True      
B = True and False     
C = False and True     
D = False and False 
print(A)  
print(B) 
print(C)
print(D)

#Q=19 Find the result of each:True or True
A = True or True
B = True or False
C = False or True
D = False or False
print(A)  
print(B) 
print(C)
print(D)

#Q=20 Find the result of:
A = not True
B = not False
print(A)
print(B)

#Q=21 Explain in your own words:
A = True and True   
B = True or False   
C = not True      
print(A)   
print(B)
print(C)

#E. Combining Conditions
#Q=22 What is the result?
age = 25
print(age >= 18 and age <= 60)

#Q=23 What is the result?
age = 16
print(age < 18 or age > 60)

#Q=24 What is the result?
age = 20
print(not age < 18)

#Q=25 Create a program that checks whether a number is greater than 10 and less than 50.
number = 25
print(number > 10 and number < 50)

#Q=26 Create a program that checks whether a number is less than 10 or greater than 100.
number = 150
print(number < 10 or number > 100)

#Q=27 Create a program using not that reverses the result of a comparison.
number = 5
print(not number > 10)

#F. Truthiness
#Q=28 For each value, identify whether it is truthy or falsy:
A = 0
B = 1
C = -5
D = ""
E = "Python"
F = False
G = True
H = None
print(bool(A))
print(bool(B))
print(bool(C))            
print(bool(D))
print(bool(E))
print(bool(F))
print(bool(G))
print(bool(H))

#Q=29 Use bool() to check the Boolean interpretation of:
A = 0
B = 10
C = ""
D = "Hello"
E = None 
print(bool(A))                                                     
print(bool(B))
print(bool(C))  
print(bool(D))  
print(bool(E))    

#Q=30 Create a small Python program that demonstrates the difference between data type and truthiness using:
values = [0, 1, "", "Python", False, None]
for value in values:
    print(value, type(value), bool(value))                



