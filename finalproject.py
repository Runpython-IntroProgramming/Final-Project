# Rain's final project
from math import sin, cos, pi
from ggame import App, Color, LineStyle, Sprite, CircleAsset, LineAsset

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle 2: '))

a=0

def step():
    oldxpen = (R-r)*cos(a) + r*50*cos(((R/r)-1)*a)+250
    oldypen = (R-r)*sin(a) - r*50*sin(((R/r)-1)*a)+240
    global a
    a=a+0.005
    xpen = (R-r)*cos(a) + r*50*cos(((R/r)-1)*a)+250
    ypen = (R-r)*sin(a) - r*50*sin(((R/r)-1)*a)+240
    asset = CircleAsset(.5, thinline, black)
    asset2 = LineAsset(xpen-oldxpen, ypen-oldypen,thinline)
    Sprite(asset, (xpen,ypen))
    Sprite(asset2, (xpen, ypen))
    
myapp = App()
myapp.run(step)