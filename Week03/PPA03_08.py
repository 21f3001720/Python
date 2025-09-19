"""
Accept a positive integer n as input and print the first n integers on a line separated by a comma.
"""
n = int(input("Enter a Integer : "))
s = ""
for i in range(n):
    if i == 0:
        s=s+"1"
    
    else:
        s = s + "," + str(i+1)
print(s)    
