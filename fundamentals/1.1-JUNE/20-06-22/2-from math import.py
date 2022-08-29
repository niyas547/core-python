
#1) we have to add math module in each calculations
import math
r=float(input("enter the r="))
area=math.pi*r*r
print(area)
print(math.sqrt(4))
print(math.pow(2,5))

#2) we dont have to add math module in each calculations dont call the math module
from math import pi,sqrt,pow
r=float(input("ENTER THE RADIUS="))
a=pi*r*r
print(a)
print(sqrt(4))
print(pow(2,3))

# 3)* we can calculte all math modules
from math import *
r=float(input("ENTER THE RADIUS="))
a=pi*r*r
print(a)
print(sqrt(4))
print(pow(2,3))