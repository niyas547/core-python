#filter -to print filtered condition
# def even(n):
#     if(n%2==0):
#         return True
#     else:
#         return False
# lst=[1,3,4,5,6,7,8,9]
# res=filter(even,lst)
# print(list(res))


# with lambda fn
# lst=[1,2,3,4,5,7,8,9]
# res=filter(lambda n:n%2==0,lst)
# print(list(res))

#two new lists with odd and even
n=input("enter the list").split()
list1=map(int,n)
n=list(list1)
even=filter(lambda n:n%2==0 and n!=0,n)
print(list(even))
odd=filter(lambda n:n%2!=0,n)
print(list(odd))




