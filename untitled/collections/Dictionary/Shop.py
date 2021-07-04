
tot=0
shop = {
            "Laptops"  : 101 ,
            "Shoes"  : 103 ,
            "Mobiles" : 104,
            "Watches" : 105,
    }

Laptops={'Dell':45000,
            'HP':42000,
            'Lenovo':35000,
         'Macbook'  :90000
         }
Watches={"Fastrack":3000,
         "Sonata":2000,
         "Titan":1500,
        "Rolex":1500000
}
Shoes ={"Nike":5000,
         "Adidas":4000,
        "Woodland":3500,
        "Skechers":7000
        }
Mobiles ={"Samsung ":20000,
          "Redmi":13000,
          "Iphone":70000,
          "One Plus":30000
          }


while(1):
    cart=[]
    print("\n************************************ WELCOME *******************************************")
    print("Product name :"," ID")
    for i in shop:
        print(i, ":\t ", shop[i])

    print("\nThe thing that you want to buy is from which category ? please enter name as appear above : ")
    nm = input()
    if nm=="Laptops":
        x=shop.get(nm)
        print ("Product Id = ",x)
        print("Item name", " ID")
        for i in Laptops:
            print(i, "\t ", Laptops[i])
        print("Enter item name that you want to buy Please type as appear in above list  : ")
        on = input()
        if on=="Dell":
             m=Laptops.get("Dell")
             cart.append(m)
             print("Item is selected!")
        elif  on=="HP":
             m=Laptops.get("HP")
             cart.append(m)
             print("Item is selected!")
        elif  on=="Lenovo":
             m=Laptops.get("Lenovo")
             cart.append(m)
             print("Item is selected!")
        elif  on=="Macbook":
             m=Laptops.get("Macbook")
             cart.append(m)
             print("Item is selected!")
        ch = int(input("Do you want to buy more press '1' else '0' : "))
        if ch != 1:
            break


    elif nm=="Watches":
        x=shop.get(nm)
        print("Product Id = ", x)
        print("Item name", " ID")
        for i in Watches:
            print(i, "\t ", Watches[i])
        print("Enter item name that you want to buy Please type as appear in above list  : ")
        on = input()
        if on == "Fastrack":
            m = Laptops.get("Fastrack")
            cart.append(m)
            print("Item is selected!")
        elif on == "Sonata":
            m = Laptops.get("Sonata")
            print(m)
            cart.append(m)
            print("Item is selected!")
        elif on == "Titan":
            m = Laptops.get("Titan")
            cart.append(m)
            print("Item is selected!")
        elif on == "Rolex":
            m = Laptops.get("Rolex")
            cart.append(m)
            print("Item is selected!")
        ch = int(input("Do you want to buy more press '1' else '0' : "))
        if ch != 1:
            break

    elif nm=="Shoes":
        x=shop.get(nm)
        print("Product Id = ", x)
        print("Item name", " ID")
        for i in Shoes:
            print(i, "\t ", Shoes[i])
        print("Enter item name that you want to buy Please type as appear in above list  : ")
        on = input()
        if on == "Nike":
            m = Laptops.get("Nike")
            cart.append(m)
            print("Item is selected!")
        elif on == "Adidas":
            m = Laptops.get("Adidas")
            cart.append(m)
            print("Item is selected!")
        elif on == "Woodland":
            m = Laptops.get("Woodland")
            cart.append(m)
            print("Item is selected!")
        elif on == "Skechers":
            m = Laptops.get("Skechers")
            cart.append(m)
            print("Item is selected!")
        ch = int(input("Do you want to buy more press '1' else '0' : "))
        if ch != 1:
            break

    elif nm=="Mobiles":
        x=shop.get(nm)
        print("Product Id = ", x)
        print("Item name", " ID")
        for i in Mobiles:
            print(i, "\t ", Mobiles[i])
        print("Enter item name that you want to buy Please type as appear in above list  : ")
        on = input()
        if on == "Samsung":
            m = Laptops.get("Samsung")
            cart.append(m)
            print("Item is selected!")
        elif on == "Redmi":
            m = Laptops.get("Redmi")
            cart.append(m)
            print("Item is selected!")
        elif on == "Iphone":
            m = Laptops.get("Iphone")
            cart.append(m)
            print("Item is selected!")
        elif on == "One Plus":
            m = Laptops.get("One Plus")
            cart.append(m)
            print("Item is selected!")
        ch = int(input("Do you want to buy more press '1' else '0' : "))
        if ch != 1:
            break
print(cart)
tot=0
for j in cart:
    tot = tot + j
print("You have to pay  : ", tot)


