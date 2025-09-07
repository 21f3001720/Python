#Accept two positive integers x and y as input. Print the number of digits in xy.
"""
Input :
3
5
Expected Output :
3
"""
n1 = int(input("Enter first Number : "))
n2 = int(input("Enter second Number : "))
print(len(str(n1**n2)))