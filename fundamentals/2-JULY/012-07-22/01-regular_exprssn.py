#pwrd-enter-valid or not
# 6-16
# atlease one samll lwttr a-z   [a-z]
# atleast one capital lttr  [A-Z]
# atleast on n 0-9     [0-9]
# atleast oone in @#$   [@#$]
import re
n=input("enter the password=")
l=len(n)
if (l<6) or l>16:
    print("invalid password")
elif not re.search("[a-z]",n):
    print("invalid password")
elif not re.search("[A-Z]",n):
    print("invalid passsword")
elif not re.search("[0-9]",n):
    print("invalid password")
elif not re.search("[@#$]",n):
    print("invalid password")
else:
    print("it is valid password")
