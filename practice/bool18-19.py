a = int(input("enter a number A: "))
b = int(input("enter a number B: "))
c = int(input("enter a number C: "))

# boolean 18
res = (a == b)or(a == c)or(b == c)

# boolean 19
res1 = (a == -b)or(a == -c)or(b == -c)


print("Boolean 18 Among three given integers there is at least one pair of equal ones: ", res)
print("Boolean 19 Among three given integers there is at least one pair of opposite ones: ", res1)
