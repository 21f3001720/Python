"""
Accept two positive integers a and b as input. Print the sum of all integers in the range [1000,2000], endpoints inclusive, that are divisible by both a and b. If you find no number satisfying this condition in the given range, then print 0.
"""
a = int(input("Enter a : "))
b = int(input("Enter b : "))

s = 0                            # stores sum, initialiesd to 0
for i in range(1000,2001):
    if i%a == 0 and i%b == 0:    # checks if remainder is zero for both a and b.
        s = s+i                  # if condition is satisfied number is added to sum s
print(s)