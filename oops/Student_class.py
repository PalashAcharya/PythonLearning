class Student:
    passing_marks =40
    x = 3
    def __init__(self,name="",sem=1,roll_num=0,obtained_marks=0):
        self.name = name
        self.sem = sem
        self.roll_num=roll_num
        self.obtained_marks= obtained_marks
    @classmethod
    def Get_passing_marks(cls):
        return cls.passing_marks
    @classmethod
    def Modifyx(cls):
        cls.x = cls.x +1 
        return cls.x
    
    def print_data(self):
        print("The Name is:",self.name," ","The semester is:",self.sem," ","The Roll Number is:",self.roll_num," ","The marks obtained is:",self.obtained_marks)
s1 = Student("Palash",1,3,50)
s1.print_data()
s2=Student("Yash",3,7,80)
s2.print_data()
s3 = Student()
s3.print_data()
print(Student.Get_passing_marks())
print(s1.Get_passing_marks())
print(Student.Modifyx())
print(Student.Modifyx())