x = int(input("Enter the length of the first side of the triangle:"))

y = int(input("Enter the length of the second side of the triangle:"))

z= int(input("Enter the length of the third side of the triangle:"))

if(x+y>z and y+z>x and x+z>y):
    print("It is a valid triangle")
else:
    print("It is not a valid triangle")                              
