"""
Accept a positive integer n as input and print the sum of the first n terms of the series:

1 + (1+2) + (1+2+3) + (1+2+3+4) + ⋯

The first term in the series is 1, the second term is (1+2), the third term is (1+2+3), and so on.
"""
n = int(input("Enter a positive Integer : "))
sum = 0
for i in range(1,n+1):
    for j in range(1,i+1):
        sum += j
print(sum)