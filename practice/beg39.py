import math
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
c = int(input("Enter number c : "))

d = b*b-4*a*c
d1=pow(d, 1/2)
x1=(-b - d1)/(2*a)
x2=(-b + d1)/(2*a)


print(f"in the  quadratic equation {a}·x2 + {b}x + {c} = 0  x1 = {x1} and x2 = {x2}") 