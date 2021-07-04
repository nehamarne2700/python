import pandas as pd

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

df=pd.read_excel('Account_Data.xlsx')
print(df)
writer=pd.ExcelWriter('Account_Data.xlsx',engine='openpyxl',mode='a')
while(True):
    print("*"*100)
    print(' '*20+'WELCOME TO ACCOUNTS'+' '*20)
    print('\n'+' '*30+'MENU'+' '*30)
    print('1:Add Account Details\n2:Read Account Details\n3:Transfer Money\n4:Exit')
    ch=int(input('Enter Your Choice : '))
    if(ch==1):
        print('Enter Account Details : ')
        a1 = Account(int(input('Enter account number:')), input('Enter customer name:'), int(input('Enter balance:')))
        norow=df.shape[0]
        for i in range(norow):
            print('infor')
            l1=list(df.iloc[i])
            df1=pd.DataFrame({'Acc_No':[l1[0]],'Name':[l1[1]],'Balance':[l1[2]]})
            df1.to_excel(writer,startrow=0+i,startcol=0)
        df1=pd.DataFrame({'Acc_No':[a1.ano],'Name':[a1.cname],'Balance':[a1.bal]})
        df1.to_excel(writer,startrow=i,startcol=0)
        writer.save()
        print('Data Added Sucessfully...')
    elif(ch==4):
        print('Thank you....Closing Program..')
        break
    else:
        print('Invalid Choice..Pls re-enter')
        continue