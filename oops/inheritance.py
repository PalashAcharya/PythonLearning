class Student:
    def __init__(self,name="",id=0,address="",marks=0):
        self._name = name
        self._id = id
        self._address = address
        self._marks= marks
    def Setname(self,name):
        self._name = name
    def Getname(self):
        return self._name
    def Setid(self,id):
        self._id =id
    def Getid(self):
        return self._id
    def Setaddress(self,add):
        self._address=add
    def Getaddress(self):
        return self._address
    def SetMarks(self,marks):
        self._marks = marks
    def Getmarks(self):
        return self._marks 
    name = property(Getname,Setname)
    id = property(Getid,Setid)
    address = property(Getaddress,Setaddress)
    marks = property(Getmarks,SetMarks)


class Teacher(Student):
    def __init__(self,salary=0):
        self._salary = salary
    def Setsalary(self,salary):
        self._salary = salary 
    def Getsalary(self):
        return self._salary
    salary = property(Getsalary,Setsalary)
     
t1 = Teacher()
t1.name = "Rohan Das"
t1.id = 101
t1.address = "5th Avenue, Springtown city,Tx 23008"
t1.salary = 10000
print("Teacher details\nName:",t1.name,"\nid:",t1.id,"\naddress:",t1.address,"\nsalary:",t1.salary)
s1 = Student()
s1.name = "Palash S Acharya"
s1.id = 2
s1.address = "101 street, Judges Bungalow rd, Bodakdev, Ahmedabad"
s1.marks = 85
print("Student Details\nName:",s1.name,"\nid:",s1.id,"\naddress:",s1.address,"\nmarks:",s1.marks)