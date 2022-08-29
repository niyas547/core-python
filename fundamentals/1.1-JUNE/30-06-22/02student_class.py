# class student marks
class student:
    def readdata(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3
    def tottal(self):
        tottal=self.mark1+self.mark2+self.mark3
        print("THE TOTAL MARK IS=",tottal)
std1=student()
std2=student()
std3=student()
std1.readdata(23,34,45)
std2.readdata(45,67,89)
std3.readdata(44,67,90)
std1.tottal()
std2.tottal()
std3.tottal()