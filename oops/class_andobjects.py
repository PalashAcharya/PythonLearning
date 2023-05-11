class Students:
    def __init__(self):
        self.name = "Vishnu"
        self.age = 20
        self.marks = 900
        print("I am from init")
    def talk(self):
        print("Hi, I am,",self.name)
        print("My age is,",self.age)
        print("My marks are:",self.marks)

student1 = Students()
student2 = Students()
student1.talk()
print(type(student1))
student1.name = "Ram"
student1.talk()
student2.talk()

