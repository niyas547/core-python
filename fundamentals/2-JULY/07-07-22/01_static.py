# static variable or class variable and static function
# all object shared value is called class variable
# and the function display in class variable is called static function
class student:
    studentcount=0
    def __init__(self,n,r):
        self.name=n
        self.roll=r
        student.studentcount+=1
    def displaycount():
        print("tottal strength is=",student.studentcount)
    def display(self):
        print("name=",self.name)
        print("roll=",self.roll)
s1=student("ram",23)
s2=student("raju",24)
s3=student("niyas",25)
s1.display()
s2.display()
s2.display()
# print("number of students is=",student.studentcount)
# or
student.displaycount()