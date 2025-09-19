""" Accept a real number x as input and print the greatest integer less than or equal to x on the first line, followed by the smallest integer greater than or equal to x on the second line. """
x = float(input())
print(int(x//1))
print(int(x//1)+1)