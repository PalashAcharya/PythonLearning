import math
class Circle:
    count = 0
    @classmethod
    def Updatecount(cls):
        cls.count = cls.count+1
    def __init__(self,radius=0):
        self._radius=radius
        Circle.Updatecount()
    def setter(self,value):
        self._radius = value
    def getter(self):
        return self._radius
    def area(self):
        return math.pi*self._radius*self._radius
    def circumference(self):
        return 2*math.pi*self._radius
    radius = property(getter,setter)

circ1 = Circle()
circ1.radius= 3
print(circ1.area())
print(circ1.circumference())
circ2 = Circle()
circ2.radius = 4
print(circ2.area())
print(circ2.circumference())
print(Circle.count)