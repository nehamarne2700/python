Products={
    "WomenCloths":{
        "shiffon saree":20000,"Cotton Kurta":900,"Blue Jeans":700,"Formal Top":400
    },
    "MenCloths":{
        "Cotton Shirt":500,"Track Pants":500,"T-Shirt":400
    },
    "Electronics":{
        "Orient Ceiling Fan":1000,
        "Radio7.I":1200,
        "Hair Dryer":1400,
        "Fridge":50000,
        "Washing Machine":65000
    },
    "Beauty":{
        "Primer":300,
        "Eye Liner":200,
        "Foundation":650,
        "Lipstick":380
    },
    "Home":{
        "teapoy":2100,
        "Stool":4000,
        "Tea Set":5200,
        "Crocary":6300
    }
}

customers=[]

while(1):
    i=1
    print('\n------------------------- Welcome To E-Shop ------------------------\n')
    for x in Products.keys():
        print(i," --> ",x)
        i+=1
    print(i,' --> My Cart Info\n0 --> EXIT ')
    ch=int(input("Enter your choice : "))
    if(ch==1):
        while(1):
            print('\n   Women Cloths   \n')
            i=1
            keys=list(Products['WomenCloths'].keys())
            val=list(Products['WomenCloths'].values())
            for k in range(len(keys)):
                print("\t", end="")
                print(i,"] ",keys[k], " : ", val[k])
                i+=1
            print('** Enter 0 to EXIT')
            ch = int(input("\tEnter which product you want to buy : "))
            if(ch>len(keys)):
                print('Invalid Product...')
            elif(ch==0):
                break
            else:
                CustomerInfo = {
                    "id": 0,
                    "Cart": [[],[]],
                    "Bill": 0
                }
                flag=0
                id = int(input('Enter customer id'))
                for i in range(0, len(customers)):
                    if customers[i].get("id") == id:
                        flag=1
                        print("\nAlready Existing Customer ")
                        customers[i]['Cart'][0].append(keys[ch - 1])
                        customers[i]['Cart'][1].append(val[ch - 1])
                        tot=customers[i]['Bill']+val[ch-1]
                        customers[i]['Bill']=tot
                        print('Added to cart..')
                if(flag==0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(keys[ch-1])
                    CustomerInfo['Cart'][1].append(val[ch - 1])
                    CustomerInfo['Bill']=val[ch-1]
                    customers.append(CustomerInfo)
                    print('Added to cart..')

            ch = int(input("Do you want to continue [ Women cloths ]...Press 1..."))
            if ch != 1:
                break
                    

    elif(ch==2):
        while (1):
            i = 1
            print("\n    Men Cloths   \n")
            keys = list(Products['MenCloths'].keys())
            val = list(Products['MenCloths'].values())
            for k in range(len(keys)):
                print("\t", end="")
                print(i, "] ", keys[k], " : ", val[k])
                i += 1
            print('** Enter 0 to EXIT')
            ch = int(input("\tEnter which product you want to buy : "))
            if (ch > len(keys)):
                print('Invalid Product...')
            elif (ch == 0):
                break
            else:
                CustomerInfo = {
                    "id": 0,
                    "Cart": [[], []],
                    "Bill": 0
                }
                flag = 0
                id = int(input('Enter customer id'))
                for i in range(0, len(customers)):
                    if customers[i].get("id") == id:
                        flag = 1
                        print("\nAlready Existing Customer ")
                        customers[i]['Cart'][0].append(keys[ch - 1])
                        customers[i]['Cart'][1].append(val[ch - 1])
                        tot = customers[i]['Bill'] + val[ch - 1]
                        customers[i]['Bill'] = tot
                        print('Added to cart..')
                if (flag == 0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(keys[ch - 1])
                    CustomerInfo['Cart'][1].append(val[ch - 1])
                    CustomerInfo['Bill'] = val[ch - 1]
                    customers.append(CustomerInfo)
                    print('Added to cart..')

            ch = int(input("Do you want to continue [ Men cloths ]...Press 1..."))
            if ch != 1:
                break


    elif (ch == 3):
        while (1):
            print("\n    Electronics   \n")
            i = 1
            keys = list(Products['Electronics'].keys())
            val = list(Products['Electronics'].values())
            for k in range(len(keys)):
                print("\t", end="")
                print(i, "] ", keys[k], " : ", val[k])
                i += 1
            print('** Enter 0 to EXIT')
            ch = int(input("\tEnter which product you want to buy : "))
            if (ch > len(keys)):
                print('Invalid Product...')
            elif (ch == 0):
                break
            else:
                CustomerInfo = {
                    "id": 0,
                    "Cart": [[], []],
                    "Bill": 0
                }
                flag = 0
                id = int(input('Enter customer id'))
                for i in range(0, len(customers)):
                    if customers[i].get("id") == id:
                        flag = 1
                        print("\nAlready Existing Customer ")
                        customers[i]['Cart'][0].append(keys[ch - 1])
                        customers[i]['Cart'][1].append(val[ch - 1])
                        tot = customers[i]['Bill'] + val[ch - 1]
                        customers[i]['Bill'] = tot
                        print('Added to cart..')
                if (flag == 0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(keys[ch - 1])
                    CustomerInfo['Cart'][1].append(val[ch - 1])
                    CustomerInfo['Bill'] = val[ch - 1]
                    customers.append(CustomerInfo)
                    print('Added to cart..')

            ch = int(input("Do you want to continue [ Electronics ]...Press 1..."))
            if ch != 1:
                break


    elif (ch == 4):
        while (1):
            i = 1
            print('\n    Beauty   \n')
            keys = list(Products['Beauty'].keys())
            val = list(Products['Beauty'].values())
            for k in range(len(keys)):
                print("\t", end="")
                print(i, "] ", keys[k], " : ", val[k])
                i += 1
            print('** Enter 0 to EXIT')
            ch = int(input("\tEnter which product you want to buy : "))
            if (ch > len(keys)):
                print('Invalid Product...')
            elif (ch == 0):
                break
            else:
                CustomerInfo = {
                    "id": 0,
                    "Cart": [[], []],
                    "Bill": 0
                }
                flag = 0
                id = int(input('Enter customer id'))
                for i in range(0, len(customers)):
                    if customers[i].get("id") == id:
                        flag = 1
                        print("\nAlready Existing Customer ")
                        customers[i]['Cart'][0].append(keys[ch - 1])
                        customers[i]['Cart'][1].append(val[ch - 1])
                        tot = customers[i]['Bill'] + val[ch - 1]
                        customers[i]['Bill'] = tot
                        print('Added to cart..')
                if (flag == 0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(keys[ch - 1])
                    CustomerInfo['Cart'][1].append(val[ch - 1])
                    CustomerInfo['Bill'] = val[ch - 1]
                    customers.append(CustomerInfo)
                    print('Added to cart..')

            ch = int(input("Do you want to continue [ Beauty ]...Press 1..."))
            if ch != 1:
                break


    elif (ch == 5):
        while (1):
            i = 1
            print('\n    Home   \n')
            keys = list(Products['Home'].keys())
            val = list(Products['Home'].values())
            for k in range(len(keys)):
                print("\t", end="")
                print(i, "] ", keys[k], " : ", val[k])
                i += 1
            print('** Enter 0 to EXIT')
            ch = int(input("\tEnter which product you want to buy : "))
            if (ch > len(keys)):
                print('Invalid Product...')
            elif (ch == 0):
                break
            else:
                CustomerInfo = {
                    "id": 0,
                    "Cart": [[], []],
                    "Bill": 0
                }
                flag = 0
                id = int(input('Enter customer id'))
                for i in range(0, len(customers)):
                    if customers[i].get("id") == id:
                        flag = 1
                        print("\nAlready Existing Customer ")
                        customers[i]['Cart'][0].append(keys[ch - 1])
                        customers[i]['Cart'][1].append(val[ch - 1])
                        tot = customers[i]['Bill'] + val[ch - 1]
                        customers[i]['Bill'] = tot
                        print('Added to cart..')
                if (flag == 0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(keys[ch - 1])
                    CustomerInfo['Cart'][1].append(val[ch - 1])
                    CustomerInfo['Bill'] = val[ch - 1]
                    customers.append(CustomerInfo)
                    print('Added to cart..')

            ch = int(input("Do you want to continue [ Home ]...Press 1..."))
            if ch != 1:
                break

    elif(ch==6):
        flag=0
        print('\n     My Cart Info    \n')
        id=int(input('Enter Your Customer Id :'))
        for i in range(0, len(customers)):
            if customers[i].get("id") == id:
                flag = 1
                print('\nCustomer Id :',id)
                print('Cart Items :')
                for j in range(len(customers[i]['Cart'][0])):
                    print(customers[i]['Cart'][0][j],' -----> ',customers[i]['Cart'][1][j])
                print('Total Bill :',customers[i].get('Bill'))
        if(flag==0):
            print("\nNo Such Customer....")

    elif(ch==0):
        print("Thank you for visiting our E-Shop :) ")
        break
    else:
        print("Invalid choice....")

    ch=int(input("Do you want to continue Shopping...Press 1..."))
    if ch!=1:
        break



'''
id=int(input('Enter customer id'))
CustomerInfo['id']=id
customers.append(CustomerInfo)

id=int(input('Enter customer id'))
#CustomerInfo['id']=id

for i in range(0,len(customers)):
    if customers[i].get("id")==id:
        print("already exists ...")

for x,y in Products.items():
    print(x," ----> ")
    for a,b in y.items():
        print("\t",end="")
        print(a," : ",b)
'''