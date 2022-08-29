#check the year leap year or not
y=int(input("ENTER THE YEAR="))
if(y%4==0)and(y%100!=0):
    print("THE YEAR IS A LEAP YEAR")
elif(y%400==0):
    print("THE YEAR IS A LEAP YEAR")
else:
    print("THE YEAR IS NOT A LEAP YEAR")