# Rain's final project
from math import sin, cos, pi
from ggame import App, Color, LineStyle, Sprite, CircleAsset

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)


R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle r: '))
f = float(input('Pen position: '))

# f is how big the spirograph is 

#converts values of a into degrees 
# make a range from 0 to 150.

# point of pen
for a in range (0,150):
    xpen = (R-r)*cos(a) + r*50*cos(((R/r)-1)*a)+200
    ypen = (R-r)*sin(a) - r*50*sin(((R/r)-1)*a)+200
    print(xpen, ypen)
    spirograph = CircleAsset(.5, thinline, black)
    Sprite(spirograph, (xpen,ypen))



myapp = App()
myapp.run()