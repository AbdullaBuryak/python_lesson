x = int(input("enter a coordinate x : "))
y = int(input("enter a coordinate y : "))

i = x > 0 and y > 0
ii = x < 0 and y > 0
iii = x < 0 and y < 0
iv = x > 0 and y < 0



print(f"Boolean 25 The point with coordinates {x, y} is in the second coordinate quarter is ",ii)
print(f"Boolean 26 The point with coordinates {x, y} is in the fourth coordinate quarter is ",iv)
print(f"Boolean 27 The point with coordinates {x, y} is in the second or third coordinate quarter is ",ii or iii)
print(f"Boolean 28 The point with coordinates {x, y} is in the first or third coordinate quarter is ",i or iii)
