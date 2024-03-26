a = int(input("Enter number a : ") ) 
b = int(input("Enter number b : ") )

c = pow((a*a+b*b), 1/2)
p = a+b+c

print(f"The hypotenuse of right triangle is {c} and the perimeter is {p}")