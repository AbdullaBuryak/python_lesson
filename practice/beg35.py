v = abs(int(input("Enter a boat velocity in still water V :")))
u = abs(int(input("Enter a river flow velocity U ( U < V ) :")))
t1 = abs(int(input("Enter a time  boat goes along the lake during  T1 :")))
t2 = abs(int(input("Enter a time goes against stream T2 :")))


s1 = t1*v
s2 = t2*(v-u)
s = s1+s2
print(f"The distance S covered by the boat is {s}")