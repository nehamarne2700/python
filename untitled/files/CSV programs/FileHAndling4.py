import csv

class Account:
    def __init__(self,ano,cname,bal):
        self.__ano=ano
        self.__cname=cname
        self.__bal=bal

    @property
    def ano(self):
        return self.__ano

    @property
    def cname(self):
        return self.__cname

    @property
    def bal(self):
        return self.__bal

    @bal.setter
    def bal(self, bal):
        self.__bal = bal

lstcust=[]

def accept():
    n=int(input('Enter number of customers you want:'))

    for i in range(n):
        a1=Account(int(input('Enter account number:')),input('Enter customer name:'),int(input('Enter balance:')))
        lstcust.append(a1)


def store():
    with open('myfile1.csv','w',newline='') as file:
        writer1=csv.writer(file)

        for i in lstcust:
            writer1.writerow([i.ano,i.cname,i.bal])

    print('Done writing.....')


def read():

    print('-----------Customers with balance more than 2000-------------')

    with open('myfile1.csv','r') as file:
        reader=csv.reader(file)

        for row in reader:
            if int(row[2])>2000:
                print('Data',row)

def readalldata():

    with open('myfile1.csv','r') as file:
        reader=csv.reader(file)

        for row in reader:
            print('Data',row)


def transfer():
    ano1=int(input('Enter your account number:'))
    ano2 = int(input('Enter account number you want to transfer to:'))
    amount = int(input('Enter amount to transfer:'))

    for i in lstcust:
        if i.ano==ano1:
            for j in lstcust:
                if j.ano==ano2:
                    j.bal=j.bal+amount
                    i.bal=i.bal-amount
                    print(i.bal,j.bal)

                    print('Done.....')

                with open('myfile1.csv', 'w', newline='') as file:
                    writer1 = csv.writer(file)

                    writer1.writerow([i.ano, i.cname, i.bal])
                    writer1.writerow([j.ano, j.cname, j.bal])

                print('Done writing.....')


while(True):
    print('1.Accept data\n2.Write data to file\n3.Read data with bal > 2000\n4.Transfer money\n5.Read all data')
    ch=int(input('Enter your choice:'))

    if ch==1:
        accept()

    elif ch==2:
        store()

    elif ch==3:
        read()

    elif ch==4:
        transfer()

    else:
        readalldata()

    print('Do you want to continue?? press 1')
    choice=input()

    if choice!='1':
        break

