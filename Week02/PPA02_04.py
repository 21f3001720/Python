"""
Accept a point in 2D space as input and find the region in space that this point belongs to. A point could belong to one of the four quadrants, or it could be on one of the two axes, or it could be the origin. The input is given in 2 lines: the first line is the x-coordinate of the point while the second line is its y-coordinate. The possible outputs are first, second, third, fourth, x-axis, y-axis, and origin. Any other output will not be accepted. Note that all outputs should be in lower case.
"""
x = float(input("Enter x-coordinate : "))
y = float(input("Enter y-coordinate : "))
if x > 0.0 :
    if y > 0.0 :
        print("first")
    elif y < 0.0 :
        print("third")
    else:
        print("x-axis")
elif x < 0.0 :
    if y > 0.0 :
        print("second")
    elif y < 0.0 :
        print("fourth")
    else:
        print("x-axis")
else:
    if y > 0.0 :
        print("Y-axis")
    elif y < 0.0 :
        print("y-axis")
    else:
        print("origin")
