# reduce function=we can reduce the function in to a single value
# we can use any type of calculations in reduce function
# or we can use from functools import reduce-we can remove functools from the result-because it cant be call in direct
import functools
lst=[1,2,3,4,5]
res=functools.reduce(lambda x,y:x+y,lst)
print(res)


# operator
from functools import reduce
import operator
lst=[1,3,4,5,6,7]
res=reduce(operator.add,lst)
print(res)
res=reduce(operator.sub,lst)
print(res)
res=reduce(operator.mul,lst)
print(res)
res=reduce(operator.truediv,lst)
print(res)