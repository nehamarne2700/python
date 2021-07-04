fruitP=[
    {
        "name":"Mango",
        "type":"Fruit",
        "quantity":10,
        "price":250
    },
    {
        "name":"Banana",
        "type":"Fruit",
        "quantity":1,
        "price":150
    }
]
flowerP=[
    {
        "name":"Merigold",
        "type":"Flower",
        "quantity":8,
        "price":100
    }
]
vegetableP=[
    {
        "name":"Brinjel",
        "type":"Vegetable",
        "quantity":20,
        "price":80
    }
]
otherP=[
    {
        "name":"Oak",
        "type":"Other",
        "quantity":12,
        "price":350
    }
]

plants=(fruitP,flowerP,vegetableP,otherP)

customers=[]


tp=("Fruit","Flower","Vegetable","Other")

while(1):
    print("-------------------------------- G.P NURSERY -------------------------------")
    print("\n                      Welcome to our Green Park Nursery                      ")
    print("\n\t\t\tMenu")
    print("\n 1: Display All Plants \n 2: NEW Plant Entry\n 3: Purchase Plants \n 4: Update Plant Info\n 5: My Purchase \n 6: EXIT")
    ch=int(input("\n Enter Your Choice : "))

    if(ch==1):
        print("\n -------------- Plants Info -------------")
        for k in range(len(plants)):
            print("\n ",tp[k],"--->")
            for i in range(len(plants[k])):
                print("\n", i + 1, "]")
                for x, y in plants[k][i].items():
                    print("\t", x, " -> ", y)

    elif(ch==2):
        plant={
            "name": "",
            "type": "",
            "quantity":0,
            "price":0
        }
        print("\n----------- NEW PLANT ENTRY -----------")
        id=input("\n Enter Nursery Id : ")
        if(id=="123456"):
            print("\n Enter Plant Info :")
            name=str.lower(input(" Plant Name : "))
            type=int(input(" Plant Type : \t 1. Fruit\t 2. Flower\t 3. Vegetable \t 4. Other :"))

            if(type==0 or type>4):
                print(" Invalid Type..")
                break

            quantity=int(input(" Plant Quantity : "))
            price=int(input(" Plant Price : "))
            flag=0
            for i in range(len(plants[type-1])):
                if str.lower(plants[type-1][i].get("name")) == name:
                    flag=1
                    print(" Plant Already Registered .. Please Go To Update Plant In Menu To Update Plant")
                    break
            if(flag==0):
                plant["name"]=name
                plant["type"]=tp[type-1]
                plant["quantity"]=quantity
                plant["price"]=price
                plants[type-1].append(plant)
                print(" Plant Info Added Successfully ")
        else:
            print(" Invalid Nursary Id...")

    elif(ch==3):
        print("\n------------ Purchase Plant ------------")
        while(1):
            print("\n 1: Fruit Plants \n 2: Flower Plants \n 3: Vegetable Plant \n 4: Other Plant \n 5: EXIT")
            ch=int(input(" Enter Your Choice : "))
            if(ch==0 or ch>4):
                print(" Invalid choice")
                break

            for i in range(len(plants[ch-1])):
                print("\n",i+1,"]\n")
                for x,y in plants[ch-1][i].items():
                    print("\t",x," -> ",y)
            print("** Enter 0 To Exit")

            pl=int(input(" Enter Which Plant No You Want To Purchase"))
            if(pl==0 or pl>len(plants[ch-1])):
                print("Invalid choice.. ")
                break

            if(plants[ch-1][pl-1]["quantity"]==0):
                print(" Sorry .... Plant Out Of Stock ")
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
                        customers[i]['Cart'][0].append(plants[ch-1][pl-1]["name"])
                        customers[i]['Cart'][1].append(plants[ch-1][pl-1]["price"])
                        tot = customers[i]['Bill'] + plants[ch-1][pl-1]["price"]
                        customers[i]['Bill'] = tot
                        print('Added to cart..')
                if (flag == 0):
                    print('\nNew customer ')
                    CustomerInfo['id'] = id
                    CustomerInfo['Cart'][0].append(plants[ch-1][pl-1]["name"])
                    CustomerInfo['Cart'][1].append(plants[ch-1][pl-1]["price"])
                    CustomerInfo['Bill'] = plants[ch-1][pl-1]["price"]
                    customers.append(CustomerInfo)
                    print('Added to cart..')
                plants[ch-1][pl-1]['quantity']=plants[ch-1][pl-1]['quantity']-1
            ch = int(input("\nDo you want to continue [ Plant Purchase ]...Press 1..."))
            if ch != 1:

                break

    elif(ch==4):
        print("\n------------- Update Plant Info ----------")
        id=input(" Enter Nursary Id : ")
        if(id=="123456"):
            print("\n 1: Fruit Plants \n 2: Flower Plants \n 3: Vegetable Plant \n 4: Other Plant \n 5: EXIT")
            ch = int(input(" Enter Your Choice : "))
            if (ch == 0 or ch > 4):
                print(" Invalid choice")
                break

            for i in range(len(plants[ch - 1])):
                print("\n", i + 1, "]\n")
                for x, y in plants[ch - 1][i].items():
                    print("\t", x, " -> ", y)
            print("** Enter 0 To Exit")

            pl = int(input(" Enter Which Plant No You Want To Update"))
            if (pl == 0 or pl > len(plants[ch - 1])):
                print("Invalid choice.. ")
                break

            print("\n Enter New Plant Info :( Only Price And Quantity an Be Updated )")
            plants[ch-1][pl-1]["price"]=input(" Enter Price : ")
            plants[ch-1][pl-1]["quantity"]=input(" Enter Quantity : ")
            print("\nPlant Info Updated Successfully ..")


    elif(ch==5):
        flag = 0
        print('\n------------ My Purchase ------------  \n')
        id = int(input(' Enter Your Customer Id :'))
        for i in range(0, len(customers)):
            if customers[i].get("id") == id:
                flag = 1
                print('\n Customer Id :', id)
                print(' Cart Items :')
                for j in range(len(customers[i]['Cart'][0])):
                    print(customers[i]['Cart'][0][j], ' -----> ', customers[i]['Cart'][1][j])
                print(' Total Bill :', customers[i].get('Bill'))
        if (flag == 0):
            print("\n No Such Customer....")

    elif(ch==6):
        print("\n Thank You For Visiting Our G.K Nursary ..")

    ch = int(input("\nDo you want to continue [ G.K Nursary ]...Press 1..."))
    if ch != 1:
        break