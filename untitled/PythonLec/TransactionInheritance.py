Type=""
s=[]
c=[]
acc=[]
class Account:
    balance=0
    accno=0

    def getAccountData(self):

        self.accno=int(input("Enter account number : "))
        self.balance=int(input("Enter account balance :"))

    def withdraw(self):
        self.accno=int(input("Enter account number :"))
        for i in range(len(acc)):
            if self.accno== acc[i]:
                amt=float(input("Enter amount to withdraw : "))
                if amt<self.balance:
                    self.balance -= amt
                    print("Amount withdrawn !!!")
                else:
                    print("Transaction cannot be proceeded!!!")
            else:
                print("Account number is not valid!!!")

    def deposit(self):
        self.accno = int(input("Enter account number :"))
        for i in range(len(acc)):
            if self.accno == acc[i]:
                amt=float(input("Enter amount to deposit : "))
                if amt<self.balance:
                    self.balance -= amt
                    print("Amount Deposited !!!")
                else:
                    print("Transaction cannot be proceeded!!!")
            else:
                print("Account number is not valid!!!")



class saving(Account):
    Pno = 0
    adhar=0
    def setSaving(self):
        print("------------------Saving Account Details-------------------")
        Account.getAccountData(self)
        self.Pno = int(input("Enter pancard number : "))
        self.adhar=int(input("Enter aadhar number : "))
        if len(str(self.adhar))==12:
            print("Account created")
            s.append(self.accno)
            acc.append(self.accno)

        else:
            print("Aadhar number should be 12 digit!!!\nEnter the correct Details Again...")
            s[i].setSaving()

    def displaySaving(self):
        print("Account number : ",s[i].accno)
        print("Account balance : ",s[i].balance)
        print("Pancard number : ",s[i].Pno)
        print("Aadhar number : ",s[i].adhar)

class current(Account):
    busin=""
    adharn=0
    def setcurrent(self):
        print("------------------Current Account Details-------------------")
        Account.getAccountData(self)
        self.busin= str(input("Enter business name : "))
        self.adharn=int(input("Enter aadhar number : "))
        if len(str(self.adharn))==12:
            print("Account created")
            c.append(Account.accno)
            acc.append(Account.accno)
        else:
            print("Aadhar number should be 12 digit!!!")
            c[i].setcurrent()


    def displayCurrent(self):
        print("Account number : ",c[i].accno)
        print("Account balance : ",c[i].balance)
        print("Business name : ",c[i].busin)
        print("Aadhar number : ",c[i].adharn)




n=int(input("How many accounts do you want to add?"))
for i in range(n):
    print("----------Enter Account ",i+1," Details---------")
    Type = str(input("Enter account type : "))
    if Type== "saving" or Type =="Saving":
        s.append(saving())
        s[i].setSaving()
        while (1):
            print("\n1.Withdraw\n2.Deposit\n3.Display Account details")
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                s[i].withdraw()

            elif ch == 2:
                s[i].deposit()

            elif ch == 3:
                s[i].displaySaving()

            ch=int(input("do you want to continue ? press 1 otherwise press 0 : "))
            if ch!=1:
                break
    if Type== "current" or Type =="Current":
        c.append(current())
        c[i].setcurrent()
        while (1):
            print("\n1.Withdraw\n2.Deposit\n3.Display Account details")
            ch = int(input("Enter Your Choice : "))
            if ch == 1:
                c[i].withdraw()

            elif ch == 2:
                c[i].deposit()

            elif ch == 3:
                c[i].displayCurrent()

            ch=int(input("do you want to continue ? press 1 otherwise press 0 : "))
            if ch != 1:
                break








