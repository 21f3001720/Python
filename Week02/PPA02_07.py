'''
A sequence of five words is called magical if the ith word is a substring of the (i+1)th word for every i in the range 1≤i<5. Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and non-magical otherwise.

Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.
'''
str_1 = str(input("Enter word 1 : "))
str_2 = str(input("Enter word 2 : "))
str_3 = str(input("Enter word 3 : "))
str_4 = str(input("Enter word 4 : "))
str_5 = str(input("Enter word 5 : "))

if str_2.find(str_1) >= 0 and str_3.find(str_2) >= 0 and str_4.find(str_3) >= 0 and str_5.find(str_4) >= 0 :
    print("magical")
else:
    print("non_magical")
        