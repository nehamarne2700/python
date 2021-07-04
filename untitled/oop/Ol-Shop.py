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
        self.id=int(input('Enter Id : '))
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
        self.name=input('\nEnter Product Name : ')
        self.quantity=int(input('Enter Product Quantity : '))
        self.price=int(input('Enter Product Price : '))

    def putProduct(self):
        print('Name : ',self.name,'\nQuantity : ',self.quantity,'\nPrice : ',self.price)

class Bill:
    bill=0
    def calculate(self,c):
        self.bill=0
        for x in c.cart:
            self.bill=self.bill+(x.quantity*x.price)
        return self.bill

cust=[]
prod=[]
b=Bill()

prod.append(Product('Earphone',4,200))
prod.append(Product('Laptop',2,50000))
prod.append(Product('NoteBook',20,50))

while(1):
    print('------------------------ WELCOME TO E-SHOP ------------------------')
    print('\n1:Add Product\n2:Purchase Products\n3:My Cart Info\n4:EXIT')
    ch=int(input('Enter Your Choice : '))

    if(ch==1):
        p=Product('',0,0)
        p.addProduct()
        flag=0
        for n in prod:
            if p.name==n.name:
                flag=1
                print('\nSimilar Product Already Exists ..')
        if(flag==0):
            prod.append(p)
            print('\nProduct Added Successfully...')

    elif(ch==2):
        print('\n--------- Products ---------')
        i=1
        for p in prod:
            print(i,']')
            i+=1
            p.putProduct()
        print('*Enter 0 To Exit')
        no=int(input('Enter Product No You Want To Purchase : '))
        q=int(input('Enter Quantity : '))
        if(no==0 or no>len(prod) or q>prod[no-1].quantity):
            print('\nInvalid Product or Quantity..\n')
        else:
            ch=int (input('\nEnter ---> 1:Existing Customer 2:New Customer  : '))
            if(ch==1):
                flag=0
                id=int(input('\nEnter Customer Id : '))
                for x in cust:
                    if(x.id==id):
                        print('in')
                        flag=1
                        p=Product(prod[no-1].name,q,prod[no-1].price)
                        x.cart.append(p)
                        prod[no-1].quantity-=q
                        print('Added To Cart ')
                if(flag==0):
                    print('\nNo Such Customer Found ')

            elif(ch==2):
                c=Customer('',0,[])
                c.getData()
                p=Product(prod[no-1].name,q,prod[no-1].price)
                c.cart.append(p)
                prod[no-1].quantity-=q
                cust.append(c)
                print('Added To Cart ')

            else:
                print('\nInvalid Choice')

    elif(ch==3):
        flag = 0
        id = int(input('\nEnter Customer Id : '))
        for x in cust:
            if(x.id==id):
                flag = 1
                x.putData()
                print('Total Bill : ',b.calculate(x))
        if (flag == 0):
            print('\nNo Such Customer Found ')

    elif(ch==4):
        print('Thank You For Visiting ...')
        break

    else:
        print('\nInvalid Choice..')

    con=int(input('Do You Want To Continue....Press 1 '))
    if(con!=1):
        break