# #MENU DRIVEN PROGRAME
while True:
        print("...........")
        print("1=Addition")
        print("2=Substraction")
        print("3=Multliplication")
        print("4=Division")
        print("5=Exit")
        ch = int(input("ENTER THE CHOICE="))
        if(ch==1):
            a=int(input("FIRST NUMBER="))
            b=int(input("SECOND NUMBER="))
            sum=a+b
            print("THE SUM IS")
            print(a,"+",b,"=",sum)
        elif(ch==2):
            a = int(input("FIRST NUMBER="))
            b = int(input("SECOND NUMBER="))
            sub=a-b
            print("THE DIFFERENCE IS")
            print(a,"-",b,"=",sub)
        elif(ch==3):
            a = int(input("FIRST NUMBER="))
            b = int(input("SECOND NUMBER="))
            pro=a*b
            print("THE PRODUCT IS")
            print(a,"*",b,"=",pro)
        elif(ch==4):
            a = int(input("FIRST NUMBER="))
            b = int(input("SECOND NUMBER="))
            div=a/b
            print("THE DIVISION IS")
            print(a,"/",b,"=",div)
        elif(ch==5):
            break
        else:
            print("INCORRECT CHOICE")
# 2)


