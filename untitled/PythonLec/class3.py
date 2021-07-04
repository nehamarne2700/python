class Car:
    # class attribute
    color = "white"
    # instance attribute
    def __init__(self, name, price):
        self.name = name
        self.price = price

# instantiate the Car class
maruti = Car("Maruti",800000)
toyota = Car("Toyota",100000)
print('Car name is ',maruti.name,'Car price is',maruti.price)
print('Car name is ',toyota.name,'Car price is',toyota.price)
# access the class attributes
print("Car1 Color is {}".format(maruti.__class__.color))
print("Car2 Color is {}".format(toyota.__class__.color))

# access the instance attributes
print("{} price is {} ".format(maruti.name,maruti.price))
print("{} price is {} ".format(toyota.name,toyota.price))


