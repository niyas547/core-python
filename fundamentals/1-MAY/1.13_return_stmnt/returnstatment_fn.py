# return statement   #to print the function outside of the statement
def calc(a,b):
    s=a+b
    d=a-b
    m=a*b
    di=a/b
    return(s,d,m,di)
a,b,c,d=calc(6,5)
print("the sum=",a)
print("the diffrence=",b)
print("the ultiple=",c)
print("the divsion=",d)

# variable length argument
# syntax
# def variablelenth(*argument):
#     for i in argument:
#         print(i)
# variablelenth(12,20,30,34)
# variablelenth(34,56,23,45)