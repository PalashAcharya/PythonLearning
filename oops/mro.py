class Vehicle:
    def __init__(self):
        self.val = 0
    def run(self):
        return f"Generic Vehicle"
class Bike(Vehicle):
    def __init__(self):
        self.val =1
    def paddle(self):
        return f"Generic bike"
class MotorVehicle(Vehicle):
    def __init__(self):
        self.val = 2
    def move(self):
        return f"Generic Motor vehicle"
class Motorbike(MotorVehicle,Bike):
    def getval(self):
        return self.val
    def performance(self):
        return f"Generic motor bike"

print(Motorbike.mro())
obj = Motorbike()
print(obj.run())
print(obj.val)