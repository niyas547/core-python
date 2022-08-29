#1) list combrehension                         #list with condetions to create a new list with these function method
lst=['apple','banana','kiwi','orange','cherry']
newlist=[x for x in lst if "a" in x]
print(newlist)

# 2)
# print the list of words without apple
# lst=['apple','banana','kiwi','orange','cherry']
# new=[x for x in lst if "apple" not in x]
# print(new)

# 3)upper case letter
lst=['apple','banana']
new=[x.upper() for x in lst]
print(new)

# 4)print the list 0 1 2 3 4
new=[x for x in range(0,5)]
print(new)

# 5)print list with banana replace strewberry,without banana print the same list
lst=['orange','apple','banana','kiwi','cherry']
new=[x if x!="banana" else "strewerry" for x in lst]
print(new)
