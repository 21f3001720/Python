'''
You have n gold coins with you. You wish to divide this among three of your friends under the following conditions:
(1) All three of them should get a non-zero share.
(2) No two of them should get the same number of coins.
(3) You should not have any coins with you at the end of this sharing process.
The input has four lines. The first line contains the number of coins with you. The next three lines will have the share given to your three friends. All inputs shall be non-negative integers. If the division satisfies these conditions, then print the string FAIR. If not, print UNFAIR.
'''
n = int(input())
n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 > 0 and n2 > 0 and n3 > 0) and (n1 != n2 and n2 != n3 and n3 != n1) and (n1 + n2 + n3 == n) :
    print("FAIR")
else:
    print("UNFAIR")