class Parent:
    def introduce(self):
        print("Hello, I am the parent")

class Child(Parent):
    def introduce(self):
        print("Hello, I am the child")
obj1 = Parent()
obj2 = Child()
obj1.introduce()
obj2.introduce()
obj1 = obj2
obj1.introduce()