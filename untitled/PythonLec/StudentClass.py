class Student:
    print("welcome")
    rno=0
    m1=0
    m2=0
    m3=0
    tot = 0
    name = " "
    city = " "

    def setData(self):
        print("thanks..")
        self.rno=int(input("Enter reg no"))
        self.name = str(input("Enter your name"))
        self.city = str(input("Enter city"))
        self.m1 = int(input("Enter marks for subject 1"))
        self.m2 = int(input("Enter marks for subject 2"))
        self.m3 = int(input("Enter marks for subject 3"))

    def calcData(self):
        print()
        self.tot=self.m1+self.m2+self.m3;
        self.per=float(self.tot/3)

    def putData(self):
        print("Reg no \t:"+str(self.rno));
        print("Name \t:" + self.name);
        print("City \t:" + self.city);
        print("Math \t:" + str(self.m1));
        print("Elect \t:" + str(self.m2));
        print("Comp \t:" + str(self.m3))
        print("Total \t:" + str(self.tot))
        print("Percentage \t:" + str(self.per))


#for one subject

'''p=Student()
p.setData();
p.calcData();
p.putData();
'''
#Array of Object.
p=[]
for x in range(2):
    p.append(Student())

for x in p:
    x.setData()
    x.calcData()

i=1
for x in p:
    print("-------------Student"+str(i)+"---Details-------------")
    x.putData()
    i=i+1
