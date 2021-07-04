print("Enter number of cars : ")
no=int(input())
list=[]
for i in range(0,no):
    car = {
        "name": "",
        "price": ""
    }
    car["name"]=input("Enter car name: ")
    car["price"]=input("Enter car price: ")
    list.append(car)

print("name","  price")
for i in range(0,no):
    print(list[i].get("name"),"\t",list[i].get("price"))

