class student:
    def getdata(self,n,r,a):
        self.name=n
        self.roll_number=r
        self.age=a
    def display(self):
        print("NAME=",self.name)
        print("ROLL_NUMBER=",self.roll_number)
        print("AGE=",self.age)
student1=student()
student2=student()
student3=student()
student1.getdata("RAMU",23,16)
student2.getdata("RAJU",24,17)
student3.getdata("RANI",26,16)
student1.display()
student2.display()
student3.display()