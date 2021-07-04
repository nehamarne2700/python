import pickle
class Address:
    city=""
    state=""

    def inputAddress(self):
        self.city=input("Enter employee city : ")
        self.state = input("Enter employee state : ")

    def displayAddress(self):
        print("Employee city : ",self.city)
        print("Employee state : ",self.state)

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

class Employee(Address):
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

    def getId(self):
        return self.emp_id

    def getName(self):
        return self.emp_name

    def getSalary(self):
        return self.emp_salary



e1=Employee()
e2=Employee()
e1.input()

with open("binaryPickle",'bw') as picklefile:
    pickle.dump(e1,picklefile)
    print('done..')

with open("binaryPickle",'br') as picklefile:
    e2=pickle.load(picklefile)
    print('done..')

e2.display()
'''
store multiple objects

e1=Employee()
e2=Employee()

e1.input()
e2.input()

lst=list(e1,e2)

with open("binaryPickle",'bw') as picklefile:
    pickle.dump(lst,picklefile)
    print('done..')





'''