# check the string is symmetric or not   yoyo
# iokiok  abcabc
st1=input("enter the string=")
l=len(st1)
if (st1[l//2:]==st1[:l//2]):
    print("IT IS A SYMMETRIC STRING")
else:
    print("IT IS NOT A SYMMMETRIC STRING")
