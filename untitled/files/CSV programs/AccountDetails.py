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


print('Existing Employee Details : ')
with open('mycsvEmployee.csv', 'r')as file:
    read=csv.reader(file)
    #print(read)
    for emp in read:
        print(emp)


a1=Account()
n=int(input('\nenter no of employee details you want to add: '))

for i in range(n):
    a1.getData()
    with open('mycsvEmployee.csv', 'a', newline='')as file:
        writer=csv.writer(file)
        writer.writerow([a1.Name,a1.AccNO,a1.Bal])


minBal=int(input('\nEnter the minimum amount you want employees to have in their account : '))
print('\nEmployees not having minBalance = '+str(minBal)+' in their account are :')

with open('mycsvEmployee.csv', 'r')as file:
    read=csv.reader(file)
    #print(read)
    for emp in read:
        if int(emp[2])<minBal:
            print(emp)


