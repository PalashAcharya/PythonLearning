class Animals:
    def speak(self):
        pass
class Dog():
    def speak(self):
        print("Bark")
class Cat():
    def speak(self):
        print("Meow")
d1 = Dog()
c1 = Cat()
animals = [d1,c1]
print(type(animals))
for animal in animals:
    animal.speak()