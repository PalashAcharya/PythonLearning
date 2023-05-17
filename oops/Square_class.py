class Square:
    def __init__(self,length_=0):
        self.length_ = length_

    def area(self):
        return self.length_*self.length_

    def perimeter(self):
        return 4*self.length_
class Rectangle:
    def __init__(self,length_=0,breadth_=0):
        self.length_=length_
        self.breadth_= breadth_
    def area(self):
        return self.length_*self.breadth_
    def perimeter(self):
        return 2*(self.length_*self.breadth_)

square1 = Square(4)
print("The area of square 1 is:",square1.area())
print("The Perimeter of square 1 is:",square1.perimeter())
square2= Square(5)
print("The area of square 2 is:",square2.area())
print("The perimeter of square 2 is:",square2.perimeter())
rectangle1 = Rectangle(2,3)
rectangle2 = Rectangle(5,6)
print("The area of rectangle 1 is:",rectangle1.area())
print("The perimeter of rectangle 2 is :",rectangle2.perimeter())
print("The area of rectangle 2 is:",rectangle2.area())
print("The perimeter of rectangle 2 is:",rectangle2.perimeter())