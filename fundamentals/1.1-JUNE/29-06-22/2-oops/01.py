class Vehicle:
    def getdata(self,n,a):
        self.name=n
        self.mileage=a
    def display(self):
        print("NAME=",self.name)
        print("MILEAGE=",self.mileage)
car=Vehicle()
bike=Vehicle()
bus=Vehicle()
car.getdata("SHIFT",25)
bike.getdata("DUKE",45)
bus.getdata("TATS",500)
car.display()
bike.display()
bus.display()



