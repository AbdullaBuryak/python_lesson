x = abs(int(input("Enter volume of chocolates in kg :")))
a = abs(int(input("Enter cost you paid for chocolates :")))
y = abs(int(input("Enter volume of sugar candies in kg:")))
b = abs(int(input("Enter cost you paid for sugar candies:")))

ca = abs(a/x) 
cb = abs(b/y) 
d = ca/cb

print(f"""
The costs of 1 kg of chocolates is {ca}
The costs of 1 kg of sugar candies is {cb}
and chocolates are more expensive than the sugar candies in {d}  times
""")


