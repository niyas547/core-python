#4)all collection types programe
# lst=[1,3,4,5]
# print(3*lst)

# question
lst=[]
odd=[]
even=[]
lst=input("enter the list").split()
for i in lst:
    if(int(i)!=0):
        if(int(i)%2==0):
            even.append(i)
        else:
            odd.append(i)
print("even list is",even)
print("odd list is",odd)
