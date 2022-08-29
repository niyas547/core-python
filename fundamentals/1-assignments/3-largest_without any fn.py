l1=[]
l=input("enter the list").split()
# res=map(int,l)
for i in l:
    l1.append(int(i))
l=list(l1)
# l=[1,2,3,46,9,6,4,1]
large=l[0]
for i in l:
    if i>large:
        large=i
print("the largest number is=",large)

