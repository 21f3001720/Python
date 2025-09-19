"""
Accept a positive integer n as input and print the first n positive integers, one number on each line.
"""
n =int(input("Enter a number n :"))
i = 0
while i+1 <= n :
    i += 1
    print(2*i)
    