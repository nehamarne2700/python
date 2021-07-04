import Shopping.MyException

from Shopping.MyException import MyException


class Product:
    name=''
    quantity=0
    price=0

    def __init__(self,name,quantity,price):
        self.name=name
        self.quantity=quantity
        self.price=price

    def addProduct(self):
        print('\nEnter Product Details : ')
        self.name=input('\nEnter Name : ')
        try:
            self.quantity=int(input('Enter Quantity : '))
            self.price=int(input('Enter Price : '))
            if(self.quantity<0):
                raise MyException('Quantity Cannot be Negative')
            if(self.price<0):
                raise MyException('Price Cannot be Negative')
        except MyException as e:
            print(e.getMessage())

    def putProduct(self):
        print('Name : ',self.name,'\nQuantity : ',self.quantity,'\nPrice : ',self.price)

class Book(Product):
    author=''
    type=''

    def __init__(self,name,quantity,price,author,type):
        Product.__init__(self,name,quantity,price)
        self.author=author
        self.type=type

    def addProduct(self):
        Product.addProduct(self)
        self.author=input('\nEnter Book Author : ')
        self.type=input('\nEnter Book Type : ')

    def putProduct(self):
        Product.putProduct(self)
        print('\nAuthor : ',self.author,'\nBook Type : ',self.type)


class Clothing(Product):
    type=''
    size=''
    material=''
    color=''

    def __init__(self,name,quantity,price,type,size,material,color):
        Product.__init__(self,name,quantity,price)
        self.type=type
        self.size=size
        self.material=material
        self.color=color

    def addProduct(self):
        Product.addProduct(self)
        self.type = input('\nEnter Clothing Type(Casual,Formal,Traditional,etc) : ')
        self.size=input('Enter Clothing Size (Small,Medium,Large) : ')
        self.material=input('Enter Clothing Material : ')
        self.color = input('Enter Clothing Color : ')

    def putProduct(self):
        Product.putProduct(self)
        print('\nType : ',self.type,'\nSize : ',self.size,'\nMaterial : ',self.material,'\nColor : ',self.color)

class Women(Clothing):

    def __init__(self,name,quantity,price,type,size,material,color):
        Clothing.__init__(self,name,quantity,price,type,size,material,color)

    def addProduct(self):
        Clothing.addProduct(self)

    def putProduct(self):
        Clothing.putProduct(self)

class Men(Clothing):

    def __init__(self,name,quantity,price,type,size,material,color):
        Clothing.__init__(self,name,quantity,price,type,size,material,color)

    def addProduct(self):
        Clothing.addProduct(self)

    def putProduct(self):
        Clothing.putProduct(self)

class Bill:
    bill=0
    def calculate(self,c):
        self.bill=0
        for x in c.cart:
            self.bill=self.bill+(x.quantity*x.price)
        return self.bill

