'''
Consider the piece-wise function given below.

f(x)= x+2       0<x<10  
      X^2 +2    10≤x   
      0         otherwise

Accept the value of x as input and print the value of f(x) as output. Note that both the input and output are real numbers. Your code should reflect this aspect. That is, both x and f(x) should be float values.
'''
x = float(input("Enter value of x :"))
if 0 < x < 10 :
    print(x+2)
elif x >= 10:
    print((x**2)+ 2)
else:
    print(0.0)