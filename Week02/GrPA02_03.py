"""
Accept a string as input and print the vowels present in the string in alphabetical order. If the string doesn't contain any vowels, then print the string none as output. Each vowel that appears in the input string — irrespective of its case — should appear just once in lower case in the output.
"""
s = str(input("Enter some string:"))
v=""
if "a" in s.lower():
    v = v+"a"
if "e" in s.lower():
    v = v+"e"
if "i" in s.lower():
    v = v+"i"
if "o" in s.lower():
    v = v+"o"
if "u" in s.lower():
    v = v+"u"

if len(v) == 0 :
    print("none")
else:
    print(v)
