#find the number of lines in a file
f=open("new4", "r")
l=f.readlines()
c=0
for i in  l:
    c=c+1
f.close()
print(c)
