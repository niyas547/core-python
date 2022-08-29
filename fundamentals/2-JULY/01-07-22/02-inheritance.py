#child and parent has same clss name that is called overriding
class person:
    def __init__(self,n,v):
        self._name=n          #input("enter the name=")
        self.voterid=v     #int(input("enter the voter id="))
    def display(self):
        print("Name=",self._name)
        print("Voter id=",self.voterid)
class employee(person):
    def __init__(self,n,v,s,d):
        super().__init__(n,v)
        self.salary=s        #int(input("enter the salary="))
        self.post=d           #input("enter the designation=")
    def display(self):
        super().display()
        # print("NAME=",self._name)
        print("Salary=",self.salary)
        print("Designation=",self.post)
emp=employee("niyas","yh67",30000,"eng")
# emp.getdata()
# emp.getdata1()
emp.display()
# print(emp.name)
print("**************")
# emp.display()
# emp.display1()

# 3-TYPES OF SPECIFIERS
# PUBLIC-CAN BE INHERIT IN TO ALL CLASSES
# PRIVATE- CAN E INHERIT TO ONL IMMEDIATE CHILD
# STRONGLY PRIVATE-CAN NOT BE INHERITED