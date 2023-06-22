class Square:
    def __init__(self,length=0):
        self._length = length
    def setlength(self,num):
        try:
            if(num>0):
                self._length = num
            else:
                raise Negativevalue(num)
        except Negativevalue as exc:
            print(exc)
        except ValueError:
            print("Invalid data entered. Please enter a positive integer")
    def getlength(self):
        return self._length
    def area(self):
        return self._length*self._length
    def perimeter(self):
        return 4*self._length
    def __eq__(self,other):
        return self._length==other._length
    length = property(getlength,setlength)
class SquareExceptions(Exception):
    pass
class Negativevalue(SquareExceptions):
    def __init__(self,val):
        self.val = val
    def __str__(self):
        return f'Sorry cant assign value as {self.val} is a negative number'
class Rectangle:
    def __init__(self,length=0,breadth=0):
        self._length=length
        self._breadth= breadth
    def setter(self,l):
        try:
            if(l>0):
                self._length = l
            else:
                raise Negativevalue(l)
        except Negativevalue as exc:
            print(exc)
        except ValueError:
            print("Invalid data entered. Please enter a Positive integer")
    def getter(self):
        return self._length
    def setbreadth(self,b):
        try:
            if(b>0):
                self._breadth = b
            else:
                raise Negativevalue(b)
        except Negativevalue as exc:
            print(exc)
        except ValueError:
            print("Invalid data entered. Please enter a Positive Integer")
    def getbreadth(self):
        return self._breadth
    def area(self):
        return self._length*self._breadth
    def perimeter(self):
        return 2*(self._length*self._breadth)
    length = property(getter,setter)
    breadth = property(getbreadth,setbreadth)
s1 = Square()
s1.length = 10
s2 = Square()
s2.length = 10
print(s1==s2)
print(s1 is s2)
print(s1.__eq__(s2))
s3 = Square()
s3.length = -10
print(s3.area())
r1 = Rectangle()
r1.length = -2
r1.breadth = -3
print(r1.perimeter())