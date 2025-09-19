"""
Accept a string as input, convert it to lower case, sort the string in alphabetical order, and print the sorted string to the console. You can assume that the string will only contain letters.
"""
word = str(input("Enter a string : "))
word_cp = ""
for i in range(len(word)):
    word_cp = word_cp + min(word)
    word = word.replace(min(word), "")
print(word_cp)


