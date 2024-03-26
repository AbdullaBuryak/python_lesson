x1 = int(input("enter a coordinate x1 (1-8): "))
y1 = int(input("enter a coordinate y1 (1-8): "))
x2 = int(input("enter a coordinate x2 (1-8): "))
y2 = int(input("enter a coordinate y2 (1-8): "))


#Boolean36
rook = (x1 == x2)or(y1==y2)

#Boolean37
xp = x1+1
xn = x1-1
yp = y1+1
yn = y1-1

king = ((xp == x2)and(yp == y2))or((xn == x2)and(yn == y2))or((x1 == x2)and(yp == y2))or((x1 == x2)and(yn == y2))or((xp == x2)and(y1 == y2))or((xn == x2)and(y1 == y2))

#Boolean38
a = x1 - y1
b = x1 + y1
a2 = x2 - y2
b2 = x2 + y2
bishop = (a==a2)or(b==b2)

#Boolean39
queen = rook or bishop

#Boolean40
xf = x1+2 
xb = x1-2
yu = y1+2
yd = y1-2
knight = (((x2 ==xf)or(x2==xb))and((y2==yp)or(y2==yn))) or (((y2 == yu)or(y2 == yd))and((x2==xp)or(x2==xn)))


print(f"#Boolean36 A Rook can move from one square to another during one turn is ",rook)
print(f"#Boolean37 King can move from one square to another during one turn is",king)
print(f"#Boolean38 Bishop can move from one square to another during one turn is",bishop)
print(f"#Boolean39 Queen can move from one square to another during one turn is", queen)
print(f"#Boolean40 Knight can move from one square to another during one turn is", knight)
