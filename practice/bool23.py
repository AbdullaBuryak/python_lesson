num = int(input("enter a number: "))

a = num//1000
b = (num - a*1000)//100
c = (num - (a*1000 + b*100))//10
d = num%10
# Boolean 20
res1 = (a==d)and(b==c)

print("The number is read equally both from left to right and from right to left is ",res1)
