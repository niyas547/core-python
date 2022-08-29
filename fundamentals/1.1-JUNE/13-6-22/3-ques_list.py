#list check -linear search check the key in the list
# lst=[]
# lst=input("enter the list").split()
# n=int(input("enter the key"))
# key=n
# for i in lst:
#     if(int(i)==key):
#         flag=1
#         break
#     else:
#         flag=0
# if(flag==1):
#     print("found")
# else:
#     print("not found")


# 2)
lst=input("enter the list").split()
key=int(input("enter the key"))
if str(key) in lst:
    print("the key found")
else:
    print("the key not found")


