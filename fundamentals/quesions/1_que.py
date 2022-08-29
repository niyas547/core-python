# print even letter words in a string
st1=input("enter the string").split()
for i in st1:
    if len(i)%2==0:
        print(i)
    else:
        print("not even")

