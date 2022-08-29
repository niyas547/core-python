# word count

f1=open("new4", "r")
lst3=f1.read()
wcount={}
for i in lst3.split():
    print(i)
    if i not in wcount:
        wcount[i]=1
    else:
        wcount[i]+=1
print(wcount)
for key,value in wcount.items():
    print(key,":",value)