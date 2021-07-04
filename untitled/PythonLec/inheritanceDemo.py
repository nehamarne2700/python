class Account:
    accType = " "
    accNumber = 0
    accBalance = 0.0
    
    def setdata(self):
        self.accNumber =int(input("Enter account Number:\t"))
        self.accBalance = float(input("Enter account Balance:\t"))

    def settype(self,type):
        self.accType = type

    def gettype(self):
        return self.accType

    def getdata(self):
       print("Account Type:\t"+str(self.accType))
       print("Account Number:\t"+str(self.accNumber))
       print("Account Balance:\t"+str(self.accBalance))

    def getaccno(self):
        return self.accNumber

    def withdraw(self, acc_no, amt):
        if self.accNumber == acc_no and amt < self.accBalance:
            self.accBalance -= amt
            print("Amount withdrawn")
        else:
          print("Transaction cannot be proceeded!")

    def deposit(self,acc_no , amt):
        if self.accNumber == acc_no:
            self.accBalance += amt
        print("Amount deposited")

    def calc(self):
        while "true":
            print("1.Withdraw")
            print("2.Deposit")
            print("3.Display Data")
            print("4.Exit")
            ch = int(input("Enter Your Choice:\t"))


            if ch == 1:
                print(x.getaccno())
                accNo = int(input("Enter Account Number:\t"))
                amt = int(input("Enter Amount To be withdrawn:\t"))
                if x.getaccno() == accNo:
                    x.withdraw(accNo, amt)

                else:
                     print("Account Not Found!")

            elif ch == 2:
                print(x.getaccno())
                accNo = int(input("Enter Account Number:\t"))
                amt = int(input("Enter Amount To be Deposited:\t"))

                if x.getaccno() == accNo:
                   x.deposit(accNo, amt)

                else:
                    print("Account Not Found!")

            elif ch == 3:
                 if x.gettype() == "saving":
                     print("--------------Account Details------------")
                     x.getdata()
                     x.getpan()

                 elif x.gettype() == "current":
                     print("--------------Account Details------------")
                     x.getdata()
                     x.getName()

            elif ch == 4:
                print("Thank You!")
                break

            else:
                print("Wrong Choice!")


class saving(Account):
    panNo = 0

    def setpan(self):
        pan=int(input("Enter pan no."))
        if len(str(pan)) == 3:
            self.panNo=pan
        else:
            print("Pan Length must be 3!")

    def getpan(self):
        print("Pan no.:\t"+str(self.panNo))


class current(Account):
    buisName = " "

    def setName(self):
        self.buisName = str(input("Enter Buissness Name:\t"))

    def getName(self):
        print("Buissness Name:\t"+str(self.buisName))


n=int(input("How many accounts do you want to add?"))
for i in range(n):
    print(f"----------Enter Account {i+1} Details---------")
    type=str(input("Enter Type:\t"))


    if type == "saving":
        s=[]
        s.append(saving())
        for x in s:
         x.settype(type)
         x.setdata()
         x.setpan()
         print(f"-------------Account {i+1} Details-------------")
         x.getdata()
         x.getpan()
         x.calc()

    elif type == "current":
        c=[]
        c.append(current())
        for x in c:
         x.settype(type)
         x.setdata()
         x.setName()
         print(f"-------------Account {i+1} Details-------------")
         x.getdata()
         x.getName()
         x.calc()



    else:
        print("No Such Type!")

