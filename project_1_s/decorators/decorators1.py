# 1
lst=[1,2,3,4,5,6,"hai","hello"]
string_list=[str(data) for data in lst]
num_list=[num for num in string_list if num.isdigit()]
number_list=[int(number)for number in num_list]
print(number_list)
# 2
lst=[1,2,3,4,5,"hello","hai"]
num_list=[data for data in lst if isinstance(data,int)]
print(num_list)








def dec_fun(fn):
    def inner_fun(*args):
        return fn([data for data in args if isinstance(data,int)])
    return inner_fun
@dec_fun
def smart_sum(*args):
    return sum([num for num in args[0]])
print(smart_sum(10,30,23,"hello","hail"))
