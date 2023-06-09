class Father:
    def __init__(self,_property=0):
        self.f_property = _property
        print("Father constructor called")
    def display(self):
        print("Father's Property:",self.f_property)
class Son(Father):
    def __init__(self,_property,s_property):
        super().__init__(_property)
        self.s_property = s_property
        print("Son's constructor called")
    def display(self):
        super().display()
        print("Son's property:",self.s_property,"\nCombined property:",self.s_property+self.f_property)
s1 = Son(20000,70000)
s1.display()