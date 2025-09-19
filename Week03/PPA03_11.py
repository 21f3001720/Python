"""
Accept a positive integer n as input and find all solutions to the equation:

    x^2 + y^2 = z^2

subject to the following constraints:
1. x, y, and z are positive integers.
2. x < y < z < n

Print each solution triplet on one line as x,y,z, with a comma between consecutive integers. The triplets should be printed in ascending order according to the following rules:
- If x1 < x2, then (x1, y1, z1) < (x2, y2, z2)
- If x1 = x2 and y1 < y2, then (x1, y1, z1) < (x2, y2, z2)
- If x1 = x2, y1 = y2, and z1 < z2, then (x1, y1, z1) < (x2, y2, z2)

If there are no solutions satisfying the given constraints, print "NO SOLUTION" as output.
"""
n = int(input())
sol_count = 0
for x in range(1,n):
    for y in range(x+1,n):
        for z in range(y+1,n):
            if x**2 + y**2 == z**2:
                sol_count = sol_count + 1
                print(f'{x},{y},{z}')
                

if sol_count == 0 :
    print("NO SOLUTION")