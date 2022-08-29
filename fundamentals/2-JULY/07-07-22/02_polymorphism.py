# polymorphism
# overloading    1-function over loading-not support in python-"class having more than one fn with same name"
#                2-operator overloading -

class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return point(x,y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p1=point(2,4)
p2=point(4,7)
print("the point is=",p1)
print("the point is=",p1+p2)