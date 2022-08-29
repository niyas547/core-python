#dictionary    1)keys and 2)values
dict={"no":1,"ram":"manu","job":"eng"}
print(dict)
print(dict.keys())
print(dict.values())
dict["salary"]=40000      #to add
print(dict)
del dict['salary']    #values cannot be deleted only the keys can be deleted
print(dict)
print(len(dict))
print(dict.items())  # gives cmplt elements
dict.clear()
print(dict)


dict1={}
print(dict1)
dict1["roll"]=23
dict1["name"]="manu"
dict1["mark"]=70
print(dict1)
d1={"per":76,"grade":"A"}
dict1.update(d1)     #to add multiple functions
print(dict1)
# copy- same dictionary will print out
d2=d1.copy()
print(d2)
d2=dict1.copy()
print(d2)
# get perticular element using get functn
print(dict1.get("roll"))
print(dict1.get("per"))

