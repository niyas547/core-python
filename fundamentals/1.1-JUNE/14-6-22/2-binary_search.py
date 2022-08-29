#binary search
def binarysearch(list,key):
    start=0
    end=len(list)-1
    while(start<=end):
        mid=(start+end)//2
        if(int(list[mid])>key):
            end=mid-1
        elif(int(list[mid])<key):
            start=mid+1
        else:
            return mid
    return -1
list1=input("ENTER THE LIST=").split()
list1.sort()
print("THE SORTED LIST IS=",list1)
key1=int(input("ENTER THE KEY="))
res=binarysearch(list1,key1)
if(res==-1):
    print("THE ITEM NOT FOUND")
else:
    print("THE ITEM FOUND AT INDEX",res)

