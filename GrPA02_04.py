"""
You are given the dates of birth of two persons, not necessarily from the same family. Your task is to find the younger of the two. If both of them share the same date of birth, then the younger of the two is assumed to be that person whose name comes first in alphabetical order.

The input will have four lines. The first two lines correspond to the first person, while the last two lines correspond to the second person. For each person, the first line corresponds to the name and the second line corresponds to the date of birth in DD-MM-YYYY format. Your output should be the name of the younger of the two.
"""

N1 = str(input())
DOB1 = str(input())
N2 = str(input())
DOB2 = str(input())

y = ''
if int(DOB1[-4:])>int(DOB2[-4:]):
    y = N1
elif int(DOB1[-4:])<int(DOB2[-4:]):
    y = N2
else :
    if int(DOB1[3:5])>int(DOB2[3:5]):
        y = N1
    elif int(DOB1[3:5])<int(DOB2[3:5]):
        y = N2
    else :
        if int(DOB1[0:2])>int(DOB2[0:2]):
            y = N1
        elif int(DOB1[0:2])<int(DOB2[0:2]):
            y = N2
        else :
            if N1<N2 :
                y = N1
            else:
                y = N2
print(y)