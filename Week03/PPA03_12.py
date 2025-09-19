"""
Accept two strings as input and form a new string by removing all characters from the second string which are present in the first string. Print this new string as output. You can assume that all input strings will be in lower case.
"""
str1 = str(input())
str2 = str(input())
string=""
for letter in str2:
    if letter not in str1:
        string = string + letter
print(string)