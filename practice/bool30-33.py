a = int(input("enter a number A : "))
b = int(input("enter a number B : "))
c = int(input("enter a number C : "))


# Boolean 30
res1 = (a==b)and(a==c)and(b==c)
# Boolean 31
res2 = (a==b)or(a==c)and((a+b>c)and (b+c>a)and(c+a>b))
# Boolean 32
res3 = c*c == a*a + b*b
# Boolean 33
res4 = (a+b>c)and (b+c>a)and(c+a>b)

print("# Boolean 30 The triangle with sides {a}, {b}, {C} is equilateral ",res1)
print("# Boolean 31 The triangle with sides {a}, {b}, {C} is isosceles ",res2)
print("# Boolean 32 The triangle with sides {a}, {b}, {C} is right triangle ",res3)
print("# Boolean 33 The triangle with sides {a}, {b}, {C} is exists ",res4)
