import Shopping.MyException

from Shopping.MyException import MyException

class Customer:
    name = ""
    id=0
    cart=[]

    def __init__(self,name,id,cart):
        self.name=name
        self.id=int(id)
        self.cart=cart

    def getData(self):
        print('\nEnter Customer Details : ')
        self.name=input('Enter Name : ')
        try:
            self.id=int(input('Enter Id : '))
            if(self.id<0):
                raise MyException('ID Cannot be Negative')
        except MyException as e:
            print(e.getMessage())
        Address.getAddress(self)
        print('Customer Account created .... Thank You ..!!!')

    def putData(self):
        print('\nYour Account Info : ')
        print('Name : ',self.name)
        print('Id : ',self.id)
        Address.putAddress(self)
        print('\nCart :')
        if(len(self.cart)==0):
            print('\nYour Cart Is Empty...')
        else:
            i=1
            for x in self.cart:
                print(f'-------------{i}-----------')
                i+=1
                x.putProduct()

class Address:
    state=''
    city=''

    def getAddress(self):
        self.state=input('Enter State : ')
        self.city=input('Enter City : ')

    def putAddress(self):
        print('State : ',self.state)
        print('City : ',self.city)
