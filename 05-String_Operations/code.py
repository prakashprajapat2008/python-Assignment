#Part 3 — String Creation and Basic Operations
#Task 1 — Create Strings
name = "prakash"
city = "nagaur"
language = "python"
message = "i am learning python"
print(name)
print(city)
print(language)
print(message)

#Task 2 — Empty String
text = ""
print(text)
print(len(text))
print(type(text))

#Task 3 — String Information
text = "Python Programming"
print("complete string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])

#Part 4 — Indexing
#Task 4 — Positive Indexing
text = "prakash"
print("First character:", text[0])
print("second character:", text[1])
print("fifth character:", text[2])
print("last character:", text[6])

#Task 5 — Negative Indexing
text = "prakash"
print("Third-last character:", text[-3])
print("Last character:", text[-1])
print("First character:", text[-7])
print("Second-last character:", text[-2])

#Task 6 — Indexing Challenge
name = "prakash"
print("First character:", text[0])
print("First character of your last name:", text[-1])
print("last character:", text[-1])

#Part 5 — Slicing
#Task 7 — Basic Slicing
text = "Python Programming"
print("Python:", text[0:6])
print("Programming:", text[7:18])
print("Python Programming:", text[:])
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])

#Task 8 — Slicing with Step
text = "ABCDEFGHIJKL"
print("every second character.:", text[::2])
print("every third character.:", text[::3])
print("index 1 to index 8 with step 2:", text[1:9:2])
print("Reverse:", text[::-1])

#Task 9 — Slicing with Negative Indexes
text = "Python Programming"
print("Last 5 characters:", text[-5:])
print("Last 10 characters:", text[-10:])
print(" reverse using a negative step:", text[::-1])

#Task 10 — Slicing Challenge
text = "Programming"
print("first 3 characters:", text[:3])
print("last 3 characters:", text[-3:])
print("Every second character:", text[::2])
print(" reverse:", text[::-1])
print("without its first and last character:", text[1:-1])

#Part 6 — Length
#Task 11
word = "Hi"
sentence = "i am find"
sentence2 = "your welcome"
print("short word:", word)
print("length:", len(word))
print("sentence:", sentence)
print("length:", len(sentence))
print("sentence with spaces:", sentence2)
print("length:", len(sentence2))

#Task 12
text = "Python Programming"
last_index = len(text) - 1
print("Last valid positive index:", last_index)
print("Last character:", text[last_index])

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
symbol = "*"
print("3 times:", symbol*3)
print("5 times:", symbol*5)
print("10 times:", symbol*10)

#Task 17 — Pattern
symbol = "*"
print(symbol*10)
