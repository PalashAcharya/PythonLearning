class square:
    def __init__(self,length=0):
        self._length=length
    @property
    def length(self):
        return self._length
    @length.setter
    def length(self,num):
        if(num>=0):
            self._length=num
        else:
            print("Enter a valid number")
    def area(self):
        return self._length*self._length
    def perimeter(self):
        return 4*self._length
square1 = square(12)
print(square1.area())
print(square1.perimeter())
square1.length=2
print(square1.area())