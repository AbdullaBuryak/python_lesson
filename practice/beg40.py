import math
a1 = int(input("Enter number A1 : "))
a2 = int(input("Enter number A2 : "))
b1 = int(input("Enter number B1 : "))
b2 = int(input("Enter number B2 : "))
c1 = int(input("Enter number C1 : "))
c2 = int(input("Enter number C2 : "))

d = a1*b2-a2*b1
d1=pow(d, 1/2)
x = (c1*b2-c2*b1)/d
y = (a1*c2-a2*c1)/d



print(f"""
in the  quadratic equation {a1}·x + {b1}y = {c1}
                           {a2}·x + {b2}y = {c2}
                           x = {x} 
                           y = {y}
                           """) 