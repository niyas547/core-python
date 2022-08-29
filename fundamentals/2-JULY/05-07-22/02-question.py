#
#
#
#
#
#
#
class student:
    def getdata(self):
        self.roll=int(input("enter the roll="))
        self.name=input("enter the name=")
        self.course=input("enter the course=")
    def displays(self):
        print("ROLL=",self.roll)
        print("NAME=",self.name)
        print("COURSE=",self.course)
class test(student):
    def getdata1(self):
        # super().getdata()
        self.mark=int(input("enter the mark="))
    def displayt(self):
        print("MARK=",self.mark)
class sports:
    def getdata2(self):
        self.sportmark=int(input("enter the sports mark="))
    def displaysp(self):
        print("SPORTS MARK=",self.sportmark)
class result(test,sports):
    def displayg(self):
        # super().getdata1()
        # super().getdata2()
        t=self.mark+self.sportmark
        if(t>=480):
            print("FIST CLASS")
        elif(t>=360):
            print("SECOND CLASS")
        elif(t>=240):
            print("THIRD CLASS")
        else:
            print("FAILED")
g1=result()
g1.getdata()
g1.getdata1()
g1.getdata2()
print("******************************************")
g1.displays()
g1.displayt()
g1.displaysp()
g1.displayg()




