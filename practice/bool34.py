x = int(input("enter a coordinate x (1-8): "))
y = int(input("enter a coordinate y(1-8): "))

white =  ((x%2 == 1) and (y%2 ==0)) or ((x%2 == 0) and (y%2 ==1)) 

print(f"The chessboard square {x, y} is white is ",white)
