class Employee:
    empCount=0

    def __init__(self,name,salary):
        self.name=name
        self.salry=salary
        Employee.empCount+=1

    def display_Count(self):
        print('Employee count ',self.empCount)

    def display_Employee(self):
        print("Name : ",self.name," Salary : ",self.salry)

emp1=Employee("abc",2000)
emp2=Employee("def",3000)

emp1.display_Employee()
emp2.display_Employee()

print("Total employee %d" % Employee.empCount)
emp1.display_Count()