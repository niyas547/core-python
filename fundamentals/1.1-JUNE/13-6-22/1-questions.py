#temperature conversion
# c to f =9/5*c+32
# f to c =5/9*f-32
print("the temperature conversion")
print("celcious to farenheat")
print("farenheat to celcious ")
ch=int(input("enter the choice"))
if(ch==1):
    print("celcious to farenheat")
    c=float(input("enter the t in c"))
    f=(9/5)*(c+32)
    print(f)
else:
    print("farenheat to celcious")
    f=float(input("enter the t in f"))
    c=(5/9)*(f-32)
    print(c)