# Rain's final project
from math import sin, cos, radians 


R = input('Radius of circle 1: ')
r = input('Radius of circle r: ')
a = input('Angle: ')
f = input('Pen position: ')

# point of pen
xpen = (R-r)*cos(radians(a)) + rf* cos((R/r-1)a)
ypen = (R-r)*sin(radians(a)) - rf*sin((R/r-1)a)