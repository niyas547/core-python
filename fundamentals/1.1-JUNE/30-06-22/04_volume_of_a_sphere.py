# volume of a sphere
from math import pi
class sphere:
    def __init__(self):
        self.radius=float(input("enter the radius="))
    def volume(self):
        volume=4/3*pi*self.radius**3
        return volume
spr1=sphere()
spr2=sphere()
print("the volume of first sphere is =",spr1.volume())
print("the volume of second sphere is =",spr2.volume())