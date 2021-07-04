import Shopping.module1
import Shopping.module2

from Shopping.module1 import Customer
from Shopping.module2 import Product
from Shopping.module2 import Book
from Shopping.module2 import Women
from Shopping.module2 import Men
from Shopping.module2 import Bill

cust=[]
prod=[]
b=Bill()

prod.append(Book('Tenaliram',4,100,'Ramkrushn','Story'))
prod.append(Women('Top',2,500,'Formal','Medium','Cotton','Blue'))
prod.append(Book('Java Complete Reference',20,900,'Herbert Schildt','Education'))


while(1):
    print('------------------------ WELCOME TO E-SHOP ------------------------')
    print('\n1:Add Product\n2:Purchase Products\n3:My Cart Info\n4:EXIT')
    ch=int(input('Enter Your Choice : '))

    if(ch==1):
        print('----------Add Product----------')
        print('\n1:Books\n2:Clothing\n3:Exit')
        ch=int(input('\nEnter Your Choice : '))
        if(ch==1):
            b=Book('',0,0,'','')
            b.addProduct()
            prod.append(b)
            print('\nBook Added Successfully...')
        elif(ch==2):
            print('1:Women Clothing\n2:Men Clothing')
            ch=int(input('\nEnter your Choice : '))
            if(ch==1):
                w=Women('',0,0,'','','','')
                w.addProduct()
                prod.append(w)
                print('\nWomen Clothing Added Successfully')
            elif(ch==2):
                m=Men('',0,0,'','','','')
                m.addProduct()
                prod.append(m)
                print('\nMen Clothing Added Successfully')
            else:
                print('\nInvalid Choice')
        elif(ch==3):
            break
        else:
            print('\nInvalid Choice')

    elif(ch==2):
        print('\n--------- Our Products ---------')
        i=1
        for p in prod:
            if(isinstance(p,Book)):
                print('-------- Books --------')
                print(i,'] ')
                i+=1
                p.putProduct()
            elif(isinstance(p,Women)):
                print('-------- Women Clothings --------')
                print(i,'] ')
                i+=1
                p.putProduct()
            elif (isinstance(p,Men)):
                print('-------- Men Clothings --------')
                print(i, '] ')
                i += 1
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