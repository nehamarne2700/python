'''

In this tutorial i am going to talk
 inheritance in python

if we have code in dog class and in future
if we want same code code in car class then will
have to repeat this code..
'''

'''
in this tutorial we are going to talk about inheritance in 
python.
inheritance is reusing code..and its not limited to 
python,most languages support inheritance
let me show you how it works...

let say we have this dog class ,it has simple walk method,
in this method we are simply printing the walk message.
let say in real time program insted of this one
line code we gone have 10 lines of code

what in future we want a define another class sal cat ,
we want to add walk method again then wel have to repeat all 
that code  in this new class
walk this is bad..beouse we have repeted or dublicated 
our code..

in programming we have principal called dry-dont 
repeat yourself 

here is resson let say some time in future we have 
discove problem in our walk method,if we have repeated or 
dublicated this method in many other places then we have to 
comeback and fix our problem in evey single place where 
we have dublicate this code so thats why in programming 
we should not define someting twise..
 
so how can we solve this problem..
there are diffrent approces but one approce is inheritance..
will define new class mammle will move walk method in 
to mammle
'''


'''class Dog:
    def walk(self):
        print("walk")
class Cat
    def walk(self):
        print("walk")
'''
#to solve above problem ...
class Mammle:
    def walk(self):
        print("walk..")

#now dog class will inherit method from mammle class..
class Dog(Mammle):#with this dog class will inherit
    # all method define in Mammle class
    def bark(self):
        print("bark..")

class Cat(Mammle):
    # python does't allow empty method...then ether add
    # another method or add pass
    # pass basically means nothing...but we dont have
    # empty class..
    pass
#lets create object...

dog=Dog()
dog.walk()#we have walk method that is defined in mammle class...
dog.bark()

cat=Cat()
cat.walk()
