#check the words with "a" and list the words
# 1)
# lst=["apple","orange","banana","kiwi"]
# newlist=[]
# for i in lst:
#     if "a" in i:
#         newlist.append(i)
# print(newlist)
# 2)
def find(i):
    if "a" in i:
        return True
lst=["apple","banana",'orange',"kiwi"]
res=filter(find,lst)
print(list(res))


