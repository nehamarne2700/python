from security.MyException import MyException
from model.myAccount import myAccount
from service.AccountDaoAbs import AccountDaoAbs

import pymysql as pms

class AccountDao(AccountDaoAbs):
    def __init__(self):
        con=''
        cur=''

    def myConnection(self):
        self.con=pms.connect(user='root',password='root',host='127.0.0.1',database='main')
        self.cur=self.con.cursor()
        self.cur.execute('select database()')


    def createAccTable(self):
        self.myConnection()
        try:
            query = "create table Account(name varchar(20),ano int primary key,bal int);"
            i=self.cur.execute(query)
            if(i==0):
                print('Table Created..')
        except Exception as e:
            print("Table Already Exists .")

    def saveRecord(self,a):
        self.myConnection()
        query="insert into Account(name,ano,bal) values (%s,%s,%s);"
        i=self.cur.execute(query,(a.name,a.ano,a.bal))
        if(i>0):
            print(i,"data inserted..")
        self.con.commit()
        self.cur.close()
        self.con.close()

    def displayAll(self):
        self.myConnection()
        query='select * from Account;'
        i=self.cur.execute(query)
        if(i>0):
            data = self.cur.fetchall()
            print('\n','+ '*30,'\n')
            for j in range(i):
                a=myAccount(data[j][0],data[j][1],data[j][2])
                print(a)
                print()
            print('\n','+ ' *30,'\n')
        else:
            print('Table is Empty...')

        self.cur.close()
        self.con.close()

    def updateRecord(self,ano,newBal):
        self.myConnection()
        query='update Account set bal=%s where ano=%s;'
        i=self.cur.execute(query,(newBal,ano))
        if(i>0):
            print('updated record..')
        else:
            print('No Such record exists...')
        self.con.commit()
        self.cur.close()
        self.con.close()

    def searchRecord(self,ano):
        self.myConnection()
        query='select * from Account where ano=%s'
        i=self.cur.execute(query,ano)
        if (i > 0):
            data=self.cur.fetchone()
            a=myAccount(data[0],data[1], data[2])
            return a
        else:
            print('No Such record exists...')

        self.cur.close()
        self.con.close()

    def deleteRecord(self,ano):
        self.myConnection()
        query='delete from Account where ano=%s'
        i = self.cur.execute(query, (ano))
        if (i > 0):
            print('deleted record..')
        else:
            print('No Such record exists...')
        self.con.commit()
        self.cur.close()
        self.con.close()

    def checkValidAcc(self,ano):
        self.myConnection()
        query = 'select * from Account;'
        i = self.cur.execute(query)
        if (i > 0):
            data = self.cur.fetchall()
            for j in range(i):
                if(data[j][1]==ano):
                    raise MyException("Account No Already Exists")