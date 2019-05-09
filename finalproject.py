# Rain's final project
from math import sin, cos, pi
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from ggame.line import LineSegment

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle 2: '))

a=0

def step():
    global a
    if a < 1500:
        oldxpen = (R-r)*cos(a) + r*1*cos(((R/r)-1)*a)+250
        oldypen = (R-r)*sin(a) - r*1*sin(((R/r)-1)*a)+240
        #print("old: ", oldxpen, oldypen)
        a=a+0.2
        xpen = (R-r)*cos(a) + r*1*cos(((R/r)-1)*a)+250
        ypen = (R-r)*sin(a) - r*1*sin(((R/r)-1)*a)+240
        #print("new: ", xpen, ypen)
        asset = CircleAsset(.5, thinline, black)
        asset2 = LineSegment((oldxpen,oldypen), (xpen,ypen), positioning="physical")
        #Sprite(asset, (xpen,ypen))
# when does the spirograph repeat, integer numbers of R and r
# style; line style
#rainbow spirograph
# go through once, then delete and add 2 shorter lines, again and again 
    
myapp = App()
myapp.run(step)