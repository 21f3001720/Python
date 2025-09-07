"""
EvenOdd is a tech startup. Each employee at the startup is given an employee id which is a unique positive integer. On one warm Sunday evening, five employees of the company come together for a meeting and sit at a circular table:

The employees follow a strange convention. They will continue the meeting only if the following condition is satisfied.

The sum of the employee-ids of every pair of adjacent employees at the table must be an even number.

They are so lazy that they won't move around to satisfy the above condition. If the current seating plan doesn't satisfy the condition, the meeting will be canceled. You are given the employee-id of all five employees. Your task is to decide if the meeting happened or not.

The input will be five lined, each line containing an integer. The ith line will have the employee-id of Ei. The output will be a single line containing one of these two strings: YES or NO.

"""
E1 = int(input())
E2 = int(input())
E3 = int(input())
E4 = int(input())
E5 = int(input())

if (E1+E2)%2 == 0 and (E3+E2)%2 == 0 and (E3+E4)%2 == 0 and (E5+E4)%2 == 0 and (E1+E5)%2 == 0 :
    print("YES")
else:
    print("NO")