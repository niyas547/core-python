#count vowels and consonents and list that
str=input('enter the string')
v=0
s=0
c=0
lst1=[]
lst2=[]
for i in str:
    if i in "aeiouAEIOU":
        v=v+1
        lst1.append(i)
    elif(i==" "):
        s=s+1
    else:
        c=c+1
        lst2.append(i)
print("the number of vowels is",v)
print("the vowels are",lst1)
print("the number of spaces are",s)
print("thr number of consonents is",c)
print("the consonents are",lst2)
