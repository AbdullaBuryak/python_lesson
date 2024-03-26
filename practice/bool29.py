x = int(input("enter a coordinate x : "))
y = int(input("enter a coordinate y : "))
x1 = int(input("enter a coordinate x1 : "))
y1 = int(input("enter a coordinate y1 : "))
x2 = int(input("enter a coordinate x2 : "))
y2 = int(input("enter a coordinate y2 : "))

res = ((x1 <= x <= x2)and(y1 <= y <= y2)) or ((x2 <= x <= x1)and(y2 <= y <= y1))

print(f"""The point {x, y} is inside of the rectangle whose left top vertex is {x1, y1},
right bottom vertex is {x2, y2}, and sides are parallel to coordinate axes is """,res)