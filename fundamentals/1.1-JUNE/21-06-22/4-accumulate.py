#accumulate-we can print list of every iterations calculations
import itertools
s=[2,3,4,5,6]
res=itertools.accumulate(s,lambda x,y:x+y)
print(list(res))
res=itertools.accumulate(s,lambda x,y:x-y)
print(list(res))