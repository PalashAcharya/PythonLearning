a = int(input("Enter the value of first angle:"))

b = int(input("Enter the value of second angle:"))

c = int(input("Enter the value of third angle:"))

if(a+b+c==180):
    if(a<90 and b<90 and c<90):
        print("The triangle is an acute triangle")
    elif(a==90 or b==90 or c==90):
        print("The triangle is a Right angle triangle")
    else:
        print("The triangle is an obtuse Trianle")
else:
    print("It is not a triangle")                