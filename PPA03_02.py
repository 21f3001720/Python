"""
Accept a positive integer n as input and print all the factors of n, one number on each line.
"""
n =int(input("Enter a number n :"))
i = 0
while i+1 <= n :
    print((2*i)+1)
    i += 1