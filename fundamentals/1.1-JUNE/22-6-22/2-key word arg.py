# **karg-keyword arguments-any items can pass
def func(**karg):
    print(type(karg))
    for key,value in karg.items():
        print(key,":",value)
func(name="anu",age=23,gender="female")