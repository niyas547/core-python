# inheritance-inherit the properties of a parent clss
# single inheritance
class parent:
    def displayp(self):
        print("i am parent")
class child(parent):
    def displayc(self):
        print("i am child")
child1=child()
child1.displayp()
child1.displayc()