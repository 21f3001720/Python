"""
Accept a positive integer n, with n > 1, as input from the user and print all the prime factors of n in ascending order.
"""
n = int(input("Enter an Integer (>1) : "))

for i in range(2, n + 1):
    if n % i == 0:                              # checks if i is a factor
        is_prime = True
        for d in range(2, int(i ** 0.5) + 1):   #checks if i is prime
            if i % d == 0:  
                is_prime = False
                break
        if is_prime:
            print(i)

