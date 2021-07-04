from security.MyException import MyException
from model.myAccount import myAccount
from Dao.AccountDao import AccountDao

adao=AccountDao()

while(True):
    print('-'*60+'\n'+' '*28+'MENU'+' '*28+'\n'+'-'*60)
    print('\n 0 :- Create Account Table \n 1 :- Add New Account \n 2 :- Search Account \n 3 :- Display All Account \n 4 :- Update Account \n 5 :- '
          'Delete Account \n 6 :- Exit \n\n'+'-'*60)
    ch=int(input('enter your choice : '))
    if(ch==0):
        adao.createAccTable()
    elif(ch==1):
        name=str(input('Enter Name : '))
        try:
            ano=int(input('Enter Account No : '))
            adao.checkValidAcc(ano)
            bal=int(input('Enter Balance : **(balance>500)'))
            if(bal<500):
                raise MyException('Balance not valid...**Should be (balance>500)')

            a=myAccount(name,ano,bal)
            adao.saveRecord(a)

        except MyException as e:
            print(e.getMessage())

    elif(ch == 2):
        ano=int(input('Enter Account No : '))
        a=adao.searchRecord(ano)
        print('\n', '+ ' * 30, '\n')
        print(a)
        print('\n', '+ ' * 30, '\n')

    elif(ch == 3):
        adao.displayAll()

    elif(ch == 4):
        ano = int(input('Enter Account No : '))
        try:
            bal = int(input('Enter New Balance : '))
            if (bal < 500):
                raise MyException('Balance not valid...**Should be (balance>500)')

            adao.updateRecord(ano,bal)

        except MyException as e:
            print(e.getMessage())

    elif(ch==5):
        ano = int(input('Enter Account No : '))
        adao.deleteRecord(ano)
    elif(ch==6):
        print("Thank you ....Closing Program.")
        break
    else:
        print('Invalid Choice...Please Re-Enter')
        continue



