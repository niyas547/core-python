#   *
#  * *
# * * *
# n=int(input("enter the number"))
# for i in range(0,n):
#     for j in range(0,n-i-1):
#         print(end=" ")
#     for k in range(0,i+1):
#         print("*",end=" ")
#     print()

# * * *
#  * *
#   *
n=int(input("enter the number"))
for i in range(-n,0):
    for j in range(0,n+i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()