class Distance:
    def __init__(self):
        self._feet =0
        self._inches = 0
    def setinch(self,val):
        if(val<12):
            self._inches = val
        else:
            self._inches = self._inches + val%12
            self._feet = self._feet + val//12
    def getinch(self):
        return self._inches
    def getfeet(self):
        return self._feet
    def setfeet(self,value):
        self._feet = self._feet + value
    def Display(self):
        print("The distance is",self._feet,"Feet and",self._inches,"Inches")
    def Addinches(self,value):
        self._inches = self._inches + value
        if(self._inches>12):
            self._feet = self._feet + self._inches//12
            self._inches = self._inches%12
    def Addition(self, d1):
        self._feet = self._feet + d1._feet
        self._inches = self._inches + d1._inches
        if(self._inches>12):
            self._feet = self._feet + self._inches//12
            self._inches = self._inches%12
    def __eq__(self,other):                                            #https://towardsdatascience.com/comparison-in-python-is-not-as-simple-as-you-may-think-a83eec69ab54
        return self.feet==other._feet and self._inches==other._inches     
    inches = property(getinch,setinch)
    feet = property(getfeet,setfeet)
#d1 = Distance()
#d1.inches = 5
#d1.feet = 3
#d2 = Distance()
#d2.feet = 2
#d2.inches = 8
#d1.Addition(d2)
#d1.Display()
d3= Distance()
d3.feet = 2
d3.inches = 3
d4 = Distance()
d4.feet = 2
d4.inches = 3
if(d3==d4):
    print("True")
else:
    print("False")