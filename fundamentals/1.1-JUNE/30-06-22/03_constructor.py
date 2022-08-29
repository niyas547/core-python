# constructr-initialise the values to data members
# it is reppresented in        __init__
#
# class student:
#     def __init__(self,m1,m2,m3):
#         self.mark1=m1
#         self.mark2=m2
#         self.mark3=m3
#     def tottal(self):
#         tottal=self.mark1+self.mark2+self.mark3
#         return tottal
# std1=student(12,34,56)
# std2=student(34,56,78)
# print("THE TOTAL MARK OF STUDENT 1 IS=",std1.tottal())
# print("THE TOTAL MARK OF STUDENT 2 IS=",std2.tottal())




class student:
    def __init__(self,m1,m2,m3):
        self.mark1=int(input("enter mark m1="))
        self.mark2=int(input("enter mark m2="))
        self.mark3=int(input("enter mark m3="))
    def tottal(self):
        tottal=self.mark1+self.mark2+self.mark3
        return tottal
std1=student()
std2=student()
print("THE TOTAL MARK OF STUDENT 1 IS=",std1.tottal())
print("THE TOTAL MARK OF STUDENT 2 IS=",std2.tottal())
