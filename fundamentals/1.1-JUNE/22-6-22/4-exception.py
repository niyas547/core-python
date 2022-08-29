try:
   a=int(input("enter a"))
   b=int(input("enter b"))
   x=8
   print(x)
   div=a/b
   print(div)
except NameError:
    print("the variable is not correct")
except ZeroDivisionError:
    print("the division with -zero- is not possible")
# except ValueError:
#     print("the value is not possible")
except:
    print("the value is not possible")