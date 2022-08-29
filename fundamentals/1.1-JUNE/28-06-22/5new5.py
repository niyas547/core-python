f1=open("new5", "r")
lst=f1.read()
print(lst)
u=0
l=0
d=0
for i in lst:
    if(47 < ord(i) <= 57):
        d=d+1
    elif(65 <= ord(i) <= 90):
        u=u+1
    elif(97 <= ord(i) <= 122):
        l=l+1
print("the number of digits is",d)
print("the number of upper case latters is",u)
print("the number of lower case latters is",l)