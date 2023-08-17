from abc import ABC,abstractclassmethod

class Computer(ABC):
    @abstractclassmethod
    def operating_software(self):
        pass
    

class Laptop(Computer):
    def operating_software(self):
        return f"Windows"
    
class Smartphone(Computer):
    def operating_software(self):
        return f"Android"

l1 = Laptop()
#print(l1.operating_software())
s1 = Smartphone()
#print(s1.operating_software())
ListOfComputer = [l1,s1]
for computer in ListOfComputer:
    print(computer.operating_software())