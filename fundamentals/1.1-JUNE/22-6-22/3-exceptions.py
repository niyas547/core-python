# exception handing-the handling of abnormal errors is known as exception handling -the abnormal errors is known as exceptions-this is not
# -synatx errors,not programe errrors
a=int(input("enter the first number="))
b=int(input("enter the second number="))
try:
    div=a/b
    print(div)                            #suspected code
except:
    print("Division with -ZERO-  is not possible")    #exceptation code
# else:
#     print("i am in the else block")      #execute when there is no exception
finally:
    print("i am in the else block")        #execute when there is also exception or without exceptions






