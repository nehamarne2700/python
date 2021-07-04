class Account:
    print("welcome")
    account_number = 0
    account_name = " "
    account_balance = 0

    def setData(self):
        print("thanks..")
        self.account_number = int(input("Enter Account no"))
        self.account_name = str(input("Enter your Account name"))
        self.account_balance = int(input("Enter Account Balance"))

    def putData(self):
        print("Account no  \t:"+str(self.account_number))
        print("Name    \t:" + self.account_name)
        print("Balance \t:" + str(self.account_balance))

    def getaccno(self):
        return self.account_number

    def withdraw(self, acc_no , amt):
        if self.account_number == acc_no:
            self.account_balance -= amt
        print("Amount withdrawn")

    def deposit(self,acc_no , amt):
        if self.account_number == acc_no:
            self.account_balance += amt
        print("Amount deposited")

#for one subject
"""p=Account()
p.setData();
p.putData();
"""
p=[]
n = int(input("How many Account you want to add"))
for x in range(n):
    p.append(Account())

for x in p:
    x.setData()

i = 1
for x in p:
    print("-------------Account"+str(i)+"---Details-------------")
    x.putData()
    i = i+1

print("1. WithDraw")
print("2. Deposit")
ch = int(input("Enter Choice"))
if ch == 1 :
    acc_no = int(input("Enter Account Number"))
    amt = int(input("Enter amount to be withdrawn"))
    for x in p:
        if x.getaccno() == acc_no:
            x.withdraw(acc_no, amt)
        else:
            print("Account not Found")
elif ch == 2:
    acc_no = int(input("Enter Account Number"))
    amt = int(input("Enter amount to be deposit"))
    for x in p:
        if x.getaccno() == acc_no:
            x.deposit(acc_no, amt)
        else:
            print("Account not Found")
else:
    print("wrong choice")

i = 1
for x in p:
    print("-------------Account"+str(i)+"---Details-------------")
    x.putData()
    i = i+1