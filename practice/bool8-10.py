a = int(input("enter a number A: "))
b = int(input("enter a number B: "))

odd1 = a%2 == 1
odd2 = b%2 == 1

res1 = odd1 and odd2
res2 = odd1 or odd2
res3 = res2 and res1 != True


print("Rersult  number A and B is odd: ", res1)
print("Rersult  one number A or B is odd: ", res2)
print("Rersult  only one number A or B is odd: ", res3)
