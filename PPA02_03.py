'''
Accept an Integer as Input and print the time of the day. Use the following table for reference.

T<0         INVALID
0<=T<=5     NIGHT
6<=T<=11    MORNING
12<=T<=17   AFTERNOON
18<=T<=23   EVENING
T>=24       INVALID
The input will be a single line containing an Integer.
The output should be any of the strings : "INVALID, NIGHT, MORNING, AFTERNOON, EVENING, INVALID"
'''
T = int(input("Enter a integer between 0 and 24 :"))
if (T < 0) or (T>=24) :
    print("INVALID")
elif 0 <= T <= 5 :
    print("NIGHT")
elif 6 <= T <= 11 :
    print("MORNING")
elif 12 <= T <= 17 :
    print("AFTERNOON")
elif 18 <= T <= 23 :
    print("EVENING")

