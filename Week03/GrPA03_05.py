"""
Accept a phone number as input. A valid phone number should satisfy the following constraints:

1. The number should start with one of these digits: 6, 7, 8, 9.
2. The number should be exactly 10 digits long.
3. No digit should appear more than 7 times in the number.
4. No digit should appear more than 5 times in a row in the number.

For example, the number 9888888765 is invalid because the digit 8 appears more than 5 times in a row.

Print the string 'valid' if the phone number is valid. If not, print the string 'invalid'.
"""
phone = str(input())
valid = True

if (len(phone) == 10) and (phone[0] in '6789'):
    for i in range(0,5):
        if phone.count(phone[i]) > 7 :
            valid = False
            break
        if 6*phone[i] in phone :
            valid = False
else:
    valid = False            


if valid :
    print("valid")
else:
    print("invalid")