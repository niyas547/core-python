# parent-inherit child-inherit a grand child
# 1)clss student- name roll
# clss mark- m1 m2 m3
# clss grade- grade()
class student:
    def __init__(self):
        self.name=input("enter the name=")
        self.roll=int(input("enter the roll number="))
    def display(self):
        print("NAME=",self.name)
        print("ROLL=",self.roll)
class mark(student):
    def __init__(self):
        super().__init__()
        self.m1=int(input("enter the mark 1="))
        self.m2=int(input("enter the mark 2="))
        self.m3=int(input("enter the mark 3="))
    def display(self):
        print("MARK 1=",self.m2)
        print("MARK 2=",self.m2)
        print("MARK 3=",self.m3)
class grade(mark):
    def __init__(self):
        super().__init__()
    def printgrade(self):
        t=self.m1+self.m2+self.m3
        p=(t/300)*100
        if(p>=80):
            print("A GRADE")
        elif(p>=60):
            print("B GRADE")
        elif(p>=40):
            print("C GRADE")
        else:
            print("FAIL")
# std1=student("niyas",45)
# std1.display()
g1=grade()
g1.printgrade()






