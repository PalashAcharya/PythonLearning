class Square:
    def __init__(self,length=0):
        self._length = length
    def setlength(self,num):
        if(num>=0):
            self._length = num
        else:
            print("Please enter a valid number")
    def getlength(self):
        return self._length
    def area(self):
        return self._length*self._length
    def perimeter(self):
        return 4*self._length
    def __eq__(self,other):
        return self._length==other._length
    length = property(getlength,setlength)
class Rectangle:
    def __init__(self,length=0,breadth=0):
        self._length=length
        self._breadth= breadth
    def setter(self,l,):
        if(l >=0):
            self._length=l
        else:
            print("Please enter a valid number")
    def getter(self):
        return self._length
    def setbreadth(self,b):
        if(b>=0):
            self._breadth = b
        else:
            print("Enter a valid number")
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