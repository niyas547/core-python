# using reduce find largest element in a list

from functools import reduce
lst=[2,4,5,6,7,8,9]
res=reduce(lambda x,y:x if x>y else y,lst)
print(res)
res=reduce(max,lst)
print(res)