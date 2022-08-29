import math
contents=dir(math)
print(contents)

# questions
# 1 sqre of a list
def square(n):
    return n*n
lst=[1,2,3,4,5,6,7]
res=map(square,lst)
print(list(res))
#2not multiples of 5
l=[2,4,5,6,7,8,9,12,20,25,45,55]
res=filter(lambda n:n%5!=0,l)
print(list(res))
# list of multiples of 5
res=filter(lambda n:n%5==0,l)
print(list(res))