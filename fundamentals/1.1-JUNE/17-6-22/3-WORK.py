# print the list without repeating numbers
a=[10,20,20,20,30,30,40,40]
nlist=[]
for i in a:
    if i not in nlist:
        nlist.append(i)
print(nlist)
