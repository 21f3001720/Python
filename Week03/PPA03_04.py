"""
Accept a positive integer n as input, where n > 1.
Print 'PRIME' if n is a prime number, and 'NOTPRIME' otherwise.
"""
n =  int(input("Enter a positive interger (>1) : "))

prime = True                # a boolean flag initialised for prime
d = 2                       # initalised divisor d to 2
while prime and d < n:      # loops while number is prime and divisor d is less than n
    if n%d == 0 :           # checks if n is completely divisible by d
        prime = not(prime)  # if so, number is not prime
    d = d+1                 # increments divisor by +1

if prime:                   # checks condition if n is prime = True
    print("PRIME")          # if so, prints PRIME
else :
    print("NOTPRIME")       # if not, prints NOTPRIME
