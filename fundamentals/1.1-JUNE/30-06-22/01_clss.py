# usng clss find the area of a rectangle
class rectangle:
    def readdata(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        a=self.length*self.breadth
        print("THE AREA IS=",a)
rec1=rectangle()
rec2=rectangle()
rec1.readdata(10,2)
rec2.readdata(22,3)
rec1.area()
rec2.area()

