#regular expressions
# import re
# match and search
# match()-find a perticular fn at the begining of a string
# search()-it can find entire line or word in the string
import re
l="python programing is fun"
m=re.search("python",l)
if m:
    print("match found")
else:
    print("no match")

# search
# sub-search and replace
import re
zipcode="1231-3245-4554"            #   syntax (pattern,replace,string name)
result=re.sub(r"\D"," ",zipcode)    #"\D" non digits "\d" digits
print(result)

# findall()
import re
l="we 23  fgfg 345 fgd 34"
print(re.findall("\D+",l))
