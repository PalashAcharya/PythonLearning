x_coordinate = int(input("Please enter x co-ordinate:"))

y_coordinate = int(input("Please enter y co-ordinate:"))

if(x_coordinate==0 and y_coordinate==0):
    print("Your point is on the origin")
elif(x_coordinate>0 and y_coordinate>0):
    print("Your point is on the first quadrant")
elif(x_coordinate<0 and y_coordinate<0):
    print("Your point is in the third quadrant")

elif(x_coordinate>0 and y_coordinate<0):
    print("Your point is in the Fourth quadrant")
else:
    print("Your point is on the second quadrant")    