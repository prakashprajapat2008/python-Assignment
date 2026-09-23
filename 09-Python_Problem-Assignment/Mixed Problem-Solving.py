# #Python Mixed Problem-Solving — 50 Unique Questions
# #1. Digit and Character Analyzer------------------------?
# string=input("Enter Your chrracters:")
# uppercasecount=0
# lowercount=0
# spacescount=0
# specialcount=0
# digitscount=0
# for i in string:
#     if chr(65)<=i<=chr(90):
#         print("uppercase:")
#         uppercasecount+=1
#     elif chr(97)<=i<=chr(122):
#         print("lowercase:")
#         lowercount+=1
#     elif chr(48)<=i<=chr(57): 
#         print("digits:")
#         digitscount+=1
#     elif chr(32)==i:
#         print("space:")
#         spacescount+=1
#     else:
#         print("special:")
#         specialcount+=1
# if uppercasecount>lowercount and uppercasecount>digitscount and uppercasecount>spacescount and uppercasecount>specialcount:
#     print("uppercase highest:")
# elif lowercount>uppercasecount and lowercount>digitscount and lowercount>specialcount and lowercount>spacescount:
#     print("loewrcase highest:")
# elif spacescount>uppercasecount and spacescount>digitscount and spacescount>specialcount and spacescount>lowercount:
#     print("spacescount highest:")
# elif specialcount>uppercasecount and specialcount>lowercount and specialcount>digitscount and specialcount>spacescount:
#     print("specialcount highest:")
# elif digitscount>uppercasecount and digitscount>lowercount and digitscount>spacescount and digitscount>specialcount:
#     print("digitscount highest:")
# else:
#     print("Tie:")

# print("upper case count:=", uppercasecount)
# print("lower case count:=", lowercount)
# print("digits count:=", digitscount)
# print("spaces count:=", spacescount)
# print("special count:=", specialcount)



# #2. Student Performance Analyzer---------------------------------------------------------------------------------------------------------------?
# Excellent-count = 0
# Good_count = 0
# Pass_count = 0
# Fail_count = 0
# for i in range(1,11):
#     Marks = int(input("Enter Your Marks:"))
#     if Marks >=75 and Marks <=100:
#         Excellent_count+=1
#         print("Excellent")
#     elif Marks >=50 and Marks <=74:
#         Good_count+=1
#         print("Good")
#     elif Marks >=35 and Marks <=49:
#         Pass_count+=1
#         print("Pass")
#     else:
#         Pass_count+=1
#         print("Fail")

#     print("Excellentcount:", Excellent_count)
#     print("Good count:", Good_count)
#     print("Pass count:", Pass_count)
#     print("Fail count:", Fail_count)


vowelcount = 0
consonantcount = 0
digitcount = 0
specialcount = 0

sentence = input("Enter in string:-")
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

        elif j in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
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

print("Consonant points:", consonantcount)
print("Vowel points:", vowelcount)
print("Digit points:", digitcount)
print("Special points:", specialcount)








