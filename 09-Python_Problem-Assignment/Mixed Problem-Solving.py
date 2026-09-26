#Python Mixed Problem-Solving — 50 Unique Questions
#1. Digit and Character Analyzer-------------------------------------------------------------------------------------------------------------?
string=input("Enter Your chrracters:")
uppercasecount=0
lowercount=0
spacescount=0
specialcount=0
digitscount=0
for i in string:
    if chr(65)<=i<=chr(90):
        print("uppercase:")
        uppercasecount+=1
    elif chr(97)<=i<=chr(122):
        print("lowercase:")
        lowercount+=1
    elif '0' <= i <= '9':
        print("digits:")
        digitscount+=1
    elif chr(32)==i:
        print("space:")
        spacescount+=1
    else:
        print("special:")
        specialcount+=1
if uppercasecount>lowercount and uppercasecount>digitscount and uppercasecount>spacescount and uppercasecount>specialcount:
    print("uppercase highest:")
elif lowercount>uppercasecount and lowercount>digitscount and lowercount>specialcount and lowercount>spacescount:
    print("loewrcase highest:")
elif spacescount>uppercasecount and spacescount>digitscount and spacescount>specialcount and spacescount>lowercount:
    print("spacescount highest:")
elif specialcount>uppercasecount and specialcount>lowercount and specialcount>digitscount and specialcount>spacescount:
    print("specialcount highest:")
elif digitscount>uppercasecount and digitscount>lowercount and digitscount>spacescount and digitscount>specialcount:
    print("digitscount highest:")
else:
    print("Tie:")

print("upper case count:=", uppercasecount)
print("lower case count:=", lowercount)
print("digits count:=", digitscount)
print("spaces count:=", spacescount)
print("special count:=", specialcount)


#2. Student Performance Analyzer------------------------------------------------------------------------------------------------------------?
Excellent-count = 0
Good_count = 0
Pass_count = 0
Fail_count = 0
for i in range(1,11):
    Marks = int(input("Enter Your Marks:"))
    if Marks >=75 and Marks <=100:
        Excellent_count+=1
        print("Excellent")
    elif Marks >=50 and Marks <=74:
        Good_count+=1
        print("Good")
    elif Marks >=35 and Marks <=49:
        Pass_count+=1
        print("Pass")
    else:
        Pass_count+=1
        print("Fail")

    print("Excellentcount:", Excellent_count)
    print("Good count:", Good_count)
    print("Pass count:", Pass_count)
    print("Fail count:", Fail_count)


#Q=3 Word Score Calculator------------------------------------------------------------------------------------------------------------------?
vowelcount = 0
consonantcount = 0
digitcount = 0
specialcount = 0
sentence = input("Enter Your string =>")
word = sentence.split()
print(word)
highestscore = 0
highestword = ""
for i in word:
    score = 0
    for j in i:
        if j in "aeiouAEIOU":
            print("vowel")
            vowelcount += 2
            score += 2
        elif j in  "A" <= i <= "Z" or "a" <= i <= "z":
            print("consonant")
            consonantcount += 1
            score += 1
        elif chr(48) <= j <= chr(57):
            print("digits")
            digitcount += 3
            score += 3
        else:
            print("special")
            specialcount += 4
            score += 4
    print(i, "score =", score)


    if score > highestscore:
        highestscore = score
        highestword = i

print("Highest word:", highestword)
print("Highest score:", highestscore)

print("consonant points:", consonantcount)
print("Vowel points:", vowelcount)
print("Digit points:", digitcount)
print("Special points:", specialcount)


#Q=4 Password Batch Validator --------------------------------------------------------------------------------------------------------------?
lowercase = 0
uppercase = 0
number = 0
special_charecter = 0
Password = input("Enter your Password => ")

for i in Password:
    if chr(65) <= i <= chr(90):
        uppercase += 1
    elif chr(97) <= i <= chr(122):
        lowercase += 1
    elif '0' <= i <= '9':
        number += 1
    else:
        special_charecter += 1
count = 0
if len(Password) >= 8:
    count += 1
if lowercase >=1:
    count += 1
if uppercase >= 1:
    count += 1
if number >= 1:
    count += 1
if special_charecter >= 1:
    count += 1
if count == 5:
    print("Strong password:, Strong ")
elif count >= 3:
    print("Medium password:, Medium")
else:
    print("Weak password:, Weak")


#Q=5 Sentence Word Analyzer -------------------------------------------------------------------------------------------------------------------?
short = 0
medium = 0
long = 0
Sentence = input("Enter a sentence => ")
words = Sentence.split()
for word in words:
    length = len(word)
    print(word, " ", length)
    if length <= 3:
        print("Short")
        short += 1
    elif length <= 6:
        print("Medium")
        medium += 1
    else:
        print("Long")
        long += 1

print("Short words:", short)
print("Medium words:", medium)
print("Long words:", long)


#Q=6 Number-String Conversion Challenge -----------------------------------------------------------------------------------------------------?
for i in range(5):
    number = int(input("Enter a number: "))

    number_string = str(number)

    even_count = 0
    odd_count = 0

    for digit in number_string:
        digit = int(digit)

        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print("Even digits:", even_count)
    print("Odd digits:", odd_count)

    if even_count > odd_count:
        print("Even")
    elif odd_count > even_count:
        print("Odd")
    else:
        print("Equal")


#Q=7 Repeated Character Report    -----------------------------------------------------------------------------------------------------------?
String=input("Enter Your String => ")
for char in String:
    count=0
    for i in String:
        if char==i:
            count+=1
    if count>1:        
        if count==2:
            print("Duplicate:=>",char,"=>",count)
        elif 3<=count<=4:
            print("Repeated:=>",char,"=>",count)   
        else:
            print("Highly Repeated:=>",char,"=>",count)     


#Q=8 Shopping Cart Analyzer    ----------------------------------------------------------------------------------------------------------------?
Total = 0
Budget = 0
Regular = 0
Premium = 0
Luxury = 0

for product in range(8):
	Price = float(input("Enter Your price of product => "))
	Total += Price

	if Price < 500:
		Budget += 1
		print("Budget")
	elif Price < 2000:
		Regular += 1
		print("Regular")
	elif Price < 5000:
		Premium += 1
		print("Premium")
	else:
		Luxury += 1
		print("Luxury")

average = Total/8

print("The Total Price:", Total)
print("The Budget products:", Budget)
print("The Regular products:", Regular)
print("The Premium products:", Premium)
print("The Luxury products:", Luxury)
print("The average products Price:", average)


#Q=9 Character Position Challenge  -------------------------------------------------------------------------------------------------------------?
Position = 0
Vowel = 0
consonant = 0
Digit = 0
Special_Characters = 0
String = input("Enter Your String =>")
for i in String:
    if Position%2==0:
        print(f"position of : {i} Even Number=>",end=" ")
    elif Position%2==1:
        print(f"position of : {i} Odd Number=>",end=" ")
    if i in "AEIOUaeiou":
        print("Vowel",end="")
        Vowel += 1
    elif "A" <= i <= "Z" or "a"<= i <= "z":
        print("consonant",end="")
        consonant += 1
    elif '0' <= i <= '9':
        print("Digit",end="")
        Digit += 1
    else:
        print("Special_Characters",end="")
        Special_Characters += 1
    Position += 1
    print()

print("The Vowel is:", Vowel)
print("The consonant is:", consonant)
print("The Digit is:", Digit)
print("The Special_Characters:", Special_Characters)


#Q=10  Number Pattern With Conditions   -------------------------------------------------------------------------------------------------------------?
Number = int(input("Enter Your Number =>"))
for i in range(Number):
    for j in range(1,i*2+2):
        if(j)%3==0 and (j)%5==0: 
            print("Z", end="")
        elif (j)%3==0:
            print("X",end=" ") 
        elif (j)%5==0:
            print("Y",end=" ") 
        else:   
            print(j,end=" ")
    print()    
        

            
            





    
    























