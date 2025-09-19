"""
Accept a positive integer n as input and print the sum of all prime numbers in the range [1, n], endpoints inclusive.

If there are no prime numbers in the given range, then print 0.
"""
n =  int(input("Enter a positive interger : "))
sum = 0
for i in range(1,n) :
    prime = True                    # a boolean flag initialised for prime
    d = 2                           # initalised divisor d to 2
    while prime and d < i+1:        # loops while number is prime and divisor d is less than n
        if (i+1)%d == 0 :           # checks if n is completely divisible by d
            prime = not(prime)
            break      # if so, number is not prime
        d = d+1                     # increments divisor by +1

    if prime:                       # checks condition if n is prime = True
        sum = sum + (i+1)           # if so, adds to sum
print(sum)