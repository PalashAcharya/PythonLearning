import math
i = int(input("Enter the value for inches : "))
f = i//12
p= i/12 -f
v = math.ceil(p*12)


print("The value in feet is: ", f, "feet")
print("The value in remaining inches is :", v, "inches")

