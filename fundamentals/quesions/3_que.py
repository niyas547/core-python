# check whether is perfect or not
# 1+2+3=6   its factors of 6  its perfect
# 1+2+4=7   its not factors of 8  its not perfect
n=int(input("ENTER THE NUMBER="))
s=0
for i in range(1,n):
    if (n%i==0):
        s=s+i
        print("THE FACTORS ARE=",i)
if (s==n):
    print("IT IS A PERFECT NUMBER")
else:
    print("IT IS NOT A PERFECT NUMBER")

