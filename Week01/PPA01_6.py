#Accept the registration number of a vehicle as input and print its state-code as output.
"""
Case 1

Input : TN-10-AB-2010
Expected Output : TN

Case 2 

Input : HR-15-XZ-1999
Expected Output : HR
"""
RgNo = str(input("Enter Registration No : "))
print(RgNo[:2])