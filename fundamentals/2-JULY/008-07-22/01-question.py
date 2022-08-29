# 1
#class-person
# fn-getperson(name,code)
# display-
# 2
# accouunt-inherited from person
#  fn-getaccount-(salary)
# display account
# 3
# admin-inherited from person
# fn--getadmin_(expence)
# display admin
# 4
# employee-inherited from account admin
class person:
    def getdata1(self,n,c):
        self.name=input("enter the name=")
        self.code=int(input("enter the code="))
    def display1(self):
        print("NAME=",self.name)
        print("CODE",self.code)
class account(person):
    def getdata2(self,s):
        self.salary=int(input("enter the salary="))
    def display2(self):
        print("SALARY=",self.salary)
class admin(person):
    def getdata3(self,e):
        self.expernce=int(input("enter the experience="))
    def display3(self):
        print("EXPERIENCE=",self.expernce)
class employee(account,admin):
    def display5(self):
        pass
e1=employee()
e1.getdata1("n","c")
e1.getdata2("s")
e1.getdata3("e")
e1.display1()
e1.display2()
e1.display3()

