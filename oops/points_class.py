import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def QuadrantOfPoint(self):
        if(self.x==0 and self.y==0):
            print("The point is at origin")
        elif(self.x>0 and self.y>0):
            print("The point is in first quadrant")
        elif(self.x<0 and self.y>0):
            print("The point is in second quadrant")
        elif(self.x<0 and self.y<0):
            print("The point is in third quadrant")
        else:
            print("The point is in fourth quadrant")
    @staticmethod
    def distance(A,B):
        s1 = A.x - B.x
        s2 = A.y - B.y
        dist = math.sqrt((s1*s1)+(s2*s2))
        return dist
obj = Point(2,3)
obj2 = Point(3,4)
obj.QuadrantOfPoint()
obj2.QuadrantOfPoint()
print(Point.distance(obj,obj2))