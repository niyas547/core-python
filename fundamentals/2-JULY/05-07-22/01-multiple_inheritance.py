# mutiple inheritnce-two parents
# a,b----->c
class A:
    def __init__(self):
        self.a=int(input("enter the number="))
    def display(self):
        print("a=",self.a)
class B:
    def __init__(self):
        self.b=int(input("enter the number="))
    def display(self):
        print("b=",self.b)
class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        self.c=int(input("enter the number="))
    def display(self):
        A.display(self)
        B.display(self)
        print("c=",self.c)
C1=C()
# C1.getdataA()
# C1.getdataB()
# C1.getdadaC()
# C1.displayA()
# C1.displayB()
# C1.displayC()
C1.display()