def Area_Of_Rectangle(length_,Breadth_):
    Area = length_*Breadth_
    return Area
def Perimeter_of_rectangle(length_,breadth_):
    a = length_+breadth_
    Perimeter = 2*a
    return Perimeter

length_ = int(input("Please enter length of a rectangle:"))
breadth_ = int(input("Please enter breadth of a rectangle:"))
Area = Area_Of_Rectangle(length_,breadth_)
perimeter = Perimeter_of_rectangle(length_,breadth_)
print("Area is :",Area )
print("Perimeter is:",perimeter)

