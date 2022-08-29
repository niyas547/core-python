# recursion
# a fn call by itself
# factorial of a number
# def fact(n):
#     if(n==1):
#         return 1           #4*fact(3)
#     else:                  #4*3*fact(2)
#         return n*fact(n-1) #4*3*2*fact(1)
# n=int(input("enter the number"))
# factorial=fact(n)
# print(factorial)

# sum of first n natual numbers using recursion
# def sum(n):
#     if(n==1):
#         return 1
#     else:
#         return n+sum(n-1)
# n=int(input("enter the number"))
# s=sum(n)
# print(s)

# hw-enter a string and fine number of vowels and consonents
n=input("enter the word")
v=0
s=0
c=0
for i in n:
    if i in('aeiouAEIOU'):
        v=v+1
    elif(i==" "):
        s=s+1
    else:
        c=c+1
print("the number of vowels is=",v)
print("the number of spaces is=",s)
print("the number of consonents=",c)