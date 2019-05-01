# Rain's final project
from math import sin, cos, pi


R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle r: '))
a = float(input('Angle: '))
f = float(input('Pen position: '))

# f is how big the spirograph is 

#converts values of a into radians 
an = a*180/pi

# point of pen
xpen = (R-r)*cos(a) + r*f*cos(((R/r)-1)*a)
ypen = (R-r)*sin(a) - r*f*sin(((R/r)-1)*a)
print(xpen)
print(ypen)