x1 = int(input("enter a coordinate x1 (1-8): "))
y1 = int(input("enter a coordinate y1 (1-8): "))
x2 = int(input("enter a coordinate x2 (1-8): "))
y2 = int(input("enter a coordinate y2 (1-8): "))

#black = (x==y) or ((x%2 == 1) and (y%2 ==1)) 
white =  ((x1%2 == 1) and (y1%2 ==0)) or ((x1%2 == 0) and (y1%2 ==1)) 
black = white == False
white1 =  ((x2%2 == 1) and (y2%2 ==0)) or ((x2%2 == 0) and (y2%2 ==1)) 
black1 = white1 == False

res = (white == white1)or(black == black1)


print(f"Both of the given chessboard squares have the same color is ",res)
