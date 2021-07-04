class Employee:
    emp_id=0
    emp_name=""
    emp_salary=0

    def input(self):
        self.emp_id=int(input("Enter employee id : "))
        self.emp_name = input("Enter employee name : ")
        self.emp_salary = int(input("Enter employee salary : "))
        Address.inputAddress(self)

    def display(self):
        print("Employee id : ",self.emp_id)
        print("Employee name : ",self.emp_name)
        print("Employee salary : ",self.emp_salary)
        Address.displayAddress(self)

class Address:
    city=""
    state=""

    def inputAddress(self):
        self.city=input("Enter employee city : ")
        self.state = input("Enter employee state : ")

    def displayAddress(self):
        print("Employee city : ",self.city)
        print("Employee state : ",self.state)

p=[]
n = int(input("How many Employee you want to add : "))
for x in range(n):
    p.append(Employee())

for x in p:
    x.input()

i = 1
for x in p:
    print("-------------Employee"+str(i)+"---Details-------------")
    x.display()
    i = i+1
