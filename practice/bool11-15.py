a = int(input("enter a number A: "))
b = int(input("enter a number B: "))
c = int(input("enter a number c: "))

num1 = a%2 == 0
num2 = b%2 == 0
num3 = c%2 == 0

# boolean 11
res1 = num1 == num2 == num3

# boolean 12
res2 = num1 and num2 and num3

# boolean 13
res3 = num1 or num2 or num3

# boolean 14
n1 = num1 or num3
n2 = num1 or num2
n3 = num2 or num3
res4 = ((n1 and n2 and n3)!= True) and res3

# boolean 15
res5 = (res4 !=True) and res3


print("Rersult Boolean 11 number A, B, C have equal parity: ", res1)
print("Rersult Boolean 12 number A, B, C is positive: ", res2)
print("Rersult Boolean 13 at liast one of the number A, B, C is positive: ", res3)
print("Rersult Boolean 14 exactly one of the number A, B, C is positive: ", res4)
print("Rersult Boolean 15 exactly two of the number A, B, C is positive: ", res5)
