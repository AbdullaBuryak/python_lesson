import math
x1 = int(input("Enter the point x1 : ") ) 
x2 = int(input("Enter the point x2 : ") ) 
x3 = int(input("Enter the point x3 : ") ) 
y1 = int(input("Enter the point  y1 : ") ) 
y2 = int(input("Enter the point  y2 : ") ) 
y3 = int(input("Enter the point  y3 : ") ) 

a = abs(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
b = abs(math.sqrt(pow((x3-x2),2)+pow((y3-y2),2)))
c = abs(math.sqrt(pow((x1-x3),2)+pow((y1-y3),2)))

p=(a+b+c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"The perimeter of the triangle is {p} and the area of the triangle is {S}")