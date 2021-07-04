class Account:
    name = "SBI Bank"
    print(f'  Welcome To {name}  ')
    AccNO=0
    Bal=0
    Pass=""

    def getData(self):
        print('\nEnter Account Details : ')
        self.AccNO=int(input('Enter Account No : '))
        self.Pass=input('Enter Password : ')
        self.Bal=int(input('Enter Account Balance : '))
        print('Thank You ..!!!')

    def putData(self):
        print('\nYour Account Info : ')
        print('Account No : ',self.AccNO)
        print('Balance : ',self.Bal)

    def withDraw(self):
        am = int(input('Enter Amount To Withdraw : '))
        if (am>self.Bal):
            print('Insufficient Balance ')
        else:
            self.Bal-=am
            print('\nAmount Withdraw Successful ')

    def deposite(self):
        am=int(input('Enter Amount To Deposite : '))
        self.Bal+=am
        print('Amount Deposite Successful ')

p=[]

n=int(input('Enter No Of Accounts You Want To Create : '))
for i in range(n):
    p.append(Account())
j=1
for i in p:
    print(f'Account {j}')
    i.getData()

while(1):
    print('\n-------------------MENU-----------------')
    print('\n1:Add Account \n2:Delete Account \n3:GoTO Account\n4:Exit')
    ch=int(input('\nEnter Your Choice : '))

    if(ch==1):
        a=Account()
        a.getData()
        p.append(a)
        print('Account Created Successfully...')
    elif(ch==2):
        acc=int(input('Enter Account No to Delete : '))
        pw=input('Enter Password : ')
        print(p)
        flag=0
        for x in p:
            if(x.AccNO==acc and x.Pass==pw):
                flag=1
                p.remove(x)
                print(p,' Deleted Successfully...')
        if(flag==0):
            print('\nAccount Not Found..')
    elif(ch==3):
        acc = int(input('Enter Account No : '))
        pw = input('Enter Password : ')
        flag = 0
        for x in p:
            if (x.AccNO == acc and x.Pass == pw):
                flag = 1
                x.putData()
                print('\n1:Withdraw \n2:Deposite \n3:Exit')
                ch=int(input('\nEnter Your choice : '))
                if(ch==1):
                    x.withDraw()
                elif(ch==2):
                    x.deposite()
                elif(ch==3):
                    print('Thank You ... Exiting Form Account....')
                else:
                    print('Invalid choice')

        if (flag == 0):
            print('\nAccount Not Found..')

    elif(ch==4):
        print('Thank You .... Exiting From Menu....')

    else:
        print('Invalid choice')

    con=int (input('\nDo You Want To continue [Menu]....press 1 : '))
    if(con!=1):
        break