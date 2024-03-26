a = int(input("enter a number A A != 0: "))
b = int(input("enter a number B: "))
c = int(input("enter a number C: "))

d = b*b - 4*a*c

res = d>=0 

print("The quadratic equation A·x2 + B·x + C = 0 has real roots ",res)
print(f"""
A = {a}
B = {b}
C = {c}
D = {d}

""")