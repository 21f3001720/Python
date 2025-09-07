#Accept a sequence of five single digit numbers separated by commas as input. Print the product of all five numbers.
'''
Input : 1,2,3,4,5
Expected Output : 120

'''
s = str(input("Enter digits with comma : "))
n1 = int(s[0])
n2 = int(s[2])
n3 = int(s[4])
n4 = int(s[6])
n5 = int(s[8])

print(n1*n2*n3*n4*n5)