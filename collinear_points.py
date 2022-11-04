x1 = int(input("Enter the x co-ordinate of first point:"))
y1 = int(input("Enter the y co-ordinate of first point:"))
x2= int(input("Enter the x co-ordinate of second point:"))
y2 = int(input("Enter the y co-ordinate of second point:"))
x3= int(input("Enter the x co-ordinate of third point:"))
y3 = int(input("Enter the y co-ordinate of third point:"))

ab1 = y2-y1
ab2 = x2-x1
bc1= y3-y2
bc2= x3-x2
ac1 = x3-x1
ac2 = y3-y1

_ab = ab1/ab2
_bc = bc1/bc2
_ac = ac1/ac2

if(_ab==_bc or _bc==_ac or _ab==_ac):
    print("The points are collinear")
else:
    print("The points are not collinear")    