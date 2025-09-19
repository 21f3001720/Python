"""
Accept a positive integer n as input and print a "number arrow" of size n.

For example, if n = 5, the output should be:
1
1,2
1,2,3
1,2,3,4
1,2,3,4,5
1,2,3,4
1,2,3
1,2
1

Each line contains a sequence of numbers starting from 1 up to a certain value, separated by commas.
The pattern increases from 1 to n and then decreases back to 1.
You can assume that n ≥ 2 for all test cases.
"""
n = int(input("Enter a number(greater than two) : "))
for i in range(1,2*n):
    s = ""
    for j in range(1,n-abs(n-i)+1):
        if j == n-abs(n-i):
            s=s+str(j)
        else:
            s=s+str(j)+","
    print(s)