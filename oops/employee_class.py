class Employee:
    def __init__(self, Name= "", id=0, sal=0):
        self.Name = Name
        self.id = id
        self.sal = sal
    def set(self,Name,id,sal):
        self.Name = Name
        self.id = id
        self.sal = sal

    def display_info(self):
        print(f"Employee name is {self.Name}, id is {self.id}, and Salary is {self.sal}")
employee1 = Employee()
employee1.set("palash",2,23000)
employee1.display_info()
employee2 = Employee()
employee2.display_info()  