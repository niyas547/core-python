# 1)*arg -nonkeyword argument-the function type will be in tuple -
# 2)**karg -keyword argument

# 1)
def func(*num):
    print(type(num))
    for i in num:
        print(i)
func(1,2,3,4,5,6)

# 2)find the sum of te elements pass through the function
def sum(*num):
    s=0
    for i in num:
        s=s+i
    print("sum is=",s)
sum(1,2,3,4,5)
