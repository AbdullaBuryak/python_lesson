num = int(input("enter a number: "))

a = num//100
b = (num - a*100)//10
c = num - (a*100 + b*10)

# Boolean 20
res1 = (a!=b)and(a!=c)and(b!=c)

# Boolean 21
res2 = (a < b < c)

# Boolean 22
res3 = (a < b < c)or(a > b > c)



print("Boolean 20 All digits of the number are different ", res1)
print("Boolean 21 All digits of the number are in ascending order ", res2)
print("Boolean 21 All digits of the number are in ascending or descending order ", res3)