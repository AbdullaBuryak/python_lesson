v1 = abs(int(input("Enter the velocity of the first car V1 :")))
v2 = abs(int(input("Enter the velocity of the second car V2 :")))
s = abs(int(input("Enter the initial distance between the cars :")))
t = abs(int(input("Enter a time :")))

s1 = (v1+v2)*t
s = abs(s-s1)


print(f"The distance  covered by the cars after {t} hours is {s} km")