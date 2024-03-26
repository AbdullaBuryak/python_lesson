import math
x1 = int(input("Enter the point x1 : ") ) 
x2 = int(input("Enter the point x2 : ") ) 
y1 = int(input("Enter the point  y1 : ") ) 
y2 = int(input("Enter the point  y2 : ") ) 

d = math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))

print(f"the distance between the points is {d}")