class Employee:
    def __init__(self,f_name="",m_name ="",l_name="",desig="",sal=0,comm=0):
        self._f_name = f_name
        self._m_name = m_name
        self._l_name = l_name
        self._desig = desig
        self._sal = sal
        self._commision = comm
    def Setf_name(self,f_name):
        self._f_name = f_name
    def Getf_name(self):
        return self._f_name
    def Setm_name(self,m_name):
        self._m_name = m_name
    def Getm_name(self):
        return self._m_name
    def Setl_name(self,l_name):
        self._l_name = l_name
    def Getl_name(self):
        return self._l_name
    def SetDesignation(self,desig):
        self._desig = desig
    def GetDesignation(self):
        return self._desig
    def SetSalary(self,sal):
        self._sal = sal
    def GetSalary(self):
        return self._sal
    def SetCommision(self,comm):
        self._commision = comm
    def GetCommision(self):
        return self._commision
    def NetSalary(self):
        return self._sal+self._commision
    def __str__(self):
        return f'Employee("{self._f_name}","{self._m_name}","{self._l_name}","{self._desig}",{self._sal},{self._commision})'
    First_name = property(Getf_name,Setf_name)
    Last_name = property(Getl_name,Setl_name)
    Middle_name = property(Getm_name,Setm_name)
    Designation = property(GetDesignation,SetDesignation)
    Commision = property(GetCommision,SetCommision)
    Salary = property(GetSalary,SetSalary)
class Salesman(Employee):
    def __init__(self):
        self._allowance = 0
        self._desig = "Salesman"
    def SetAllowance(self,all):
        self._allowance = all
    def GetAllowance(self):
        return self._allowance
    def NetSalary(self):
        return self._sal+self._commision+self._allowance*30
    Allowance = property(GetAllowance,SetAllowance)
obj1 = Employee("Palash","Sanjay","Acharya","salesman",10000,2000)
obj1.First_name = "Palash"
obj1.Middle_name = "Sanjay"
obj1.Last_name = "Acharya"
obj1.Salary = 10000
obj1.Commision = 2000
obj1.Designation = "salesman"
print("Details of Salesman\nName:",obj1.First_name," ",obj1.Middle_name," ",obj1.Last_name,"\nDesignation:",obj1.Designation,"\nNet salary:",obj1.NetSalary())
x = str(obj1)
print(x)
y = eval(x)
print(y)
print(type(x))
print(type(y))