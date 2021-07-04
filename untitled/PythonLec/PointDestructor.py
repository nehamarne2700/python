class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def __del__(self):
        class_name=self.__class__.__name__
        print(class_name,"destroyed")

    def show(self):
        print("hello..")


pt=Point();
pt1=Point()
pt2=pt1
pt3=pt1
print(id(pt),id(pt1),id(pt2),id(pt3))

del pt
del pt1

pt2.show()
pt3.show()