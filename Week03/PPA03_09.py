"""
Accept a positive integer n as input and print a triangle of zeros for n lines.

For each line i (1 ≤ i ≤ n), print i zeros with no spaces between consecutive zeros.
Do not print a space at the end of any line.
"""
for i in range(int(input("Enter a Integer:"))):
    print(str(0)*(i+1))