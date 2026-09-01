#python assignment
#Part 3 — String Creation and Basic Operations
#Task 1 — Create Strings
from asyncio import Task


name = "prakash"
city = "nagaur"
language = "python"
message = "i am learning python"
print(name)
print(city)
print(language)
print(message)

#Task 2 — Empty String
X = ""
print(X)
print(len(X))
print(type(X))

#Task 3 — String Information
X = "Python Programming"
print("complete string:", X)
print("Length:", len(X))
print("First character:", X[0])
print("Last character:", X[-1])
print("Third character:", X[2])
print("Second-last character:", X[-2])

#Part 4 — Indexing
#Task 4 — Positive Indexing
X = "prakash"
print("First character:", X[0])
print("second character:", X[1])
print("fifth character:", X[2])
print("last character:", X[6])

#Task 5 — Negative Indexing
X = "prakash"
print("Third-last character:", X[-3])
print("Last character:", X[-1])
print("First character:", X[-7])
print("Second-last character:", X[-2])

#Task 6 — Indexing Challenge
name = "prakash"
print("First character:", X[0])
print("First character of your last name:", X[-1])
print("last character:", X[-1])

#Part 5 — Slicing
#Task 7 — Basic Slicing
X = "Python Programming"
print("Python:", X[0:6])
print("Programming:", X[7:18])
print("Python Programming:", X[:])
print("First 5 characters:", X[:5])
print("Last 5 characters:", X[-5:])

#Task 8 — Slicing with Step
X = "ABCDEFGHIJKL"
print("every second character.:", X[::2])
print("every third character.:", X[::3])
print("index 1 to index 8 with step 2:", X[1:9:2])
print("Reverse:", X[::-1])

#Task 9 — Slicing with Negative Indexes
X = "Python Programming"
print("Last 5 characters:", X[-5:])
print("Last 10 characters:", X[-10:])
print(" reverse using a negative step:", X[::-1])

#Task 10 — Slicing Challenge
X = "Programming"
print("first 3 characters:", X[:3])
print("last 3 characters:", X[-3:])
print("Every second character:", X[::2])
print(" reverse:", X[::-1])
print("without its first and last character:", X[1:-1])

#Part 6 — Length
#Task 11
X = "Hi"
Y = "i am find"
Z = "your welcome"
print("short word:", X)
print("length:", len(X))
print("sentence:", Y)
print("length:", len(Y))
print("sentence with spaces:", Z)
print("length:", len(Z))

#Task 12
X = "Python Programming"
last_index = len(X) - 1
print("Last valid positive index:", last_index)
print("Last character:", X[last_index])

#Part 7 — Concatenation
#Task 13 — Full Name
First_Name = "prakash"
Last_Name = "kailash"
full_name = First_Name + " " + Last_Name
print(full_name)

#Task 14 — Sentence Creation
name = "prakash"
age = "18"
city = "nagaur"
language = "python"
print(name+" "+age+" "+city+" "+language)

#Task 15 — String and Integer
name = "prakash"
age = 18
print("my name is" + name)
print("my age is" + str(age))

#Part 8 — String Repetition
#Task 16
X = "*"
print("3 times:", X*3)
print("5 times:", X*5)
print("10 times:", X*10)

#Task 17 — Pattern
X = "*"
print(X*10)

#Part 9 — Case Conversion
#Task 18
X = "python programming language"
print(X.upper())
print(X.lower())
print(X.capitalize())
print(X.title())
print(X.swapcase())

#Task 19 — Case-Insensitive Comparison
X = "Python"
Y = "python"
print(X == Y)
X = X.lower()
Y = Y.lower()
print(X == Y)

#Part 10 — Searching
#Task 20 — Membership
X = "Python is a programming language"
print("Python" in X)
print("programming" in X)
print("java" in X)
print("language" in X)

#Task 21 — find()
X = "Python is a programming language"
print(X.find("python"))
print(X.find("programming"))
print(X.find("language"))
print(X.find("Java"))

#Task 22 — index()
X = "i love you my dear brother"
result = X.index("my")
print(result)

#Task 23 — Count Characters
A = "banana"
print(A.count("a"))
print(A.count("n"))
print(A.count("b"))

#Task 24 — Starts and Ends
a = "student_notes.pdf"
print(a.startswith("student"))
print(a.endswith(".pdf"))
print(a.endswith(".txt"))

#Part 11 — Replacing
#Task 25 — Replace a Word
A = "I am learning Java"
print(A.replace("Java", "Python"))

#Task 26 — Multiple Replacements
A = "apple apple apple"
print(A.replace("apple", "orange"))

#Task 27 — Limited Replacement
A = "apple apple apple"
print(A.replace("apple", "orange", 1))

#Task 28 — Check Immutability
A = "Python"
b = A.upper()
print(b)
print(A)

#Part 12 — Whitespace
#Task 29
A = "   Python Programming   "
b = A.strip()
c = A.lstrip()
d = A.rstrip()
print(b)
print(c)
print(d)

#Task 30 — User Input
#name = input("Enter your name: ")
cleaned_name = name.strip()
print("Cleaned name:", cleaned_name)

#Part 13 — Split and Join
#Task 31 — Split
A = "Python is easy to learn"
b = (A.split())
print(b)
print(" ".join(b))

#Task 32 — Split with Separator
a = "apple,banana,mango,orange"
print(a.split(","))

#Task 33 — Join
words = ["Python", "is", "easy"]
print(" ".join(words))  

#Task 34 — Join with Different Separators
words = ["Python", "is", "easy"]
print(" ".join(words))  
print("-".join(words))  
print("/".join(words))

#Part 14 — String Formatting
#Task 35 — F-String
name = "prakash"
age = 18
city = "nagaur"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

#Task 36 — Arithmetic Inside F-String
a = 10
b = 20
print(f"The sum is {a + b}.")

#Part 15 — Error Identification
#Task 37
text = "Python"
#print(text[20])
#comment: This will raise an IndexError because the index 20 is out of range for the string "Python", which has a length of 6.
print(text[5])

text = "Python"
#text[0] = "J"
#comment: This will raise a TypeError because strings in Python are immutable, and you cannot change a character at a specific index.
print("j" + text[1:])

age = 20
#print("Age: " + age)
#comment: This will raise a TypeError because you cannot concatenate a string and an integer directly. You need to convert the integer to a string first.
print("Age: " + str(age))

text = "Python"
#print(text.index("Java"))
#comment: This will raise a ValueError because the substring "Java" is not found in the string "Python". The index() method raises an error when the substring is not present.
print(text.find("Java"))

#Part 16 — Practical Challenge
#Task 38 — Name Processor
name = input("Enter your full name: ")
# 1. Remove extra spaces from beginning and end
print("Cleaned name:", name.strip())
# 2.Display the original input.
print("Original input:", name)
# 3. Display the cleaned name.
print("Cleaned name:", name.strip())
# 4. Display the name in uppercase 
print("Uppercase:", name.upper())
# 5. Display the name in lowercase
print("Lowercase:", name.lower())
# 6. Display the name in title case
print("Title case:", name.title())
# 7.Display the length of the name.
print("Length of name:", len(name.strip()))
# 8.Display the first character.
print("First character:", name.strip()[0])
# 9.Display the last character.
print("Last character:", name.strip()[-1])
# 10.Check whether the name contains a particular character.
print("Contains 'a':", 'a' in name)

#Part 17 — Practical Challenge
#Task 39 — Sentence Analyzer


