import csv
class Account:
    bankName = "SBI Bank"
    print(f'  Welcome To {bankName}  ')
    AccNO=0
    Bal=0
    Name=""

    def getData(self):
        print('\nEnter Account Details : ')
        self.Name = input('Enter Name : ')
        self.AccNO=int(input('Enter Account No : '))
        self.Bal=int(input('Enter Account Balance : '))
        print('Thank You ..!!!')

    def putData(self):
        print('\nYour Account Info : ')
        print('\nName : ',self.Name)
        print('Account No : ',self.AccNO)
        print('Balance : ',self.Bal)

a1=Account()
i=0
n=int(input('\nenter no of employee details you want to add: '))
list1=[]
for i in range(n):
    a1.getData()
    list1.append(a1)

with open('mycsvEmployee.csv', 'w', newline='')as file:
    writer=csv.writer(file)
    writer.writerow(list1)


minBal=int(input('\nEnter the minimum amount you want employees to have in their account : '))
print('\nEmployees not having minBalance = '+str(minBal)+' in their account are :')

with open('mycsvEmployee.csv', 'r')as file:
    read=csv.reader(file)
    read=list(read)
    #print(read)
    for emp in read:
        print(type(emp[i]))
        i+=1



