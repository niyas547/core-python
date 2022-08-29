#control statement
#break
# continue
# pass

# break
# for i in range(1,11):
#     if(i==4):
#         break
#     print(i)

# continue
# for i in range(1,11):
#     if(i==5):
#         continue
#     print(i)

# check a given number is prime or not

n=int(input('enter the number='))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
if(flag==1):
    print("Not prime")
else:
    print('Prime')