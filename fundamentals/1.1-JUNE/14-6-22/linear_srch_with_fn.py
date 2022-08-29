#linear search using function
def linearsearch(lst1,key):
    l=len(lst1)
    for i in range(0,l):
        if(int(lst1[i])==key):
            return i
    return -1
print("THE LIST IS")
lst=input("enter the list").split()
a=int(input("enter the key"))
key=a
res=linearsearch(lst,key)
if(res==-1):
    print("the item not found")
else:
    print("the item found",res)