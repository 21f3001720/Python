"""
Accept a positive integer as input and print the sum of the digits in the number.
"""

number = str(input())
digit_sum = 0
for digit in number:
    digit_sum = digit_sum + int(digit)
print(digit_sum)