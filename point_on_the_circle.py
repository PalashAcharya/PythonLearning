import math

p = int(input("Enter the x co-ordinate of center point:"))
q= int(input("Enter the y co-ordinate of the center point:"))
x = int(input("Enter the x co-ordinate of desired point:"))
y = int(input("Enter the y co-ordinate of the desired point:"))
r = int(input("Enter the radius of the circle:"))

s1 = p-x
s2 = q-y

d = math.sqrt((s1*s1) + (s2*s2))

if(d>r):
    print("The point is outside the circle")
elif(d<r):
    print("The point is inside the circle")
else:
    print("The point is on the circle")        