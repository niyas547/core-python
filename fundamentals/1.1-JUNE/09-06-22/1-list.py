# list spiliting
# .split()
# type the elements in space seperated
#  sum of elements of list using split -we have to convert the list in strings to integer values using type conversion
n=input("enter the elements").split()            #space seperated
print(n)
s=0
for i in n:
    s=s+int(i)
print("sum is",s)
