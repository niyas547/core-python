f1=open("new1", 'r')
lst=f1.readlines()
print(lst)
lst.reverse()
print(lst)
for i in lst:
    print(i.strip())
