# Accept a five digit number as input and print the sum of its digits as output.
"""
Case 1
Input : 12345
Expected Output : 15

Case 2
Input : 67890
Expected Output : 30

"""
num = str(input("Enter 5digit Number"))
n1 = int(num[0])
n2 = int(num[1])
n3 = int(num[2])
n4 = int(num[3])
n5 = int(num[4])

print(n1 + n2 + n3 + n4 + n5)