# Rain's final project
# Sources:
# 1. https://math.stackexchange.com/questions/823578/how-do-i-calculate-the-perodicity-of-a-spirograph-hypotrochoid
# 2. https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3

from math import sin, cos, pi, floor 
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from ggame.line import LineSegment

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)
darkorange = Color(0xD07702, 0)
thinline4 = LineStyle(1, darkorange)

listc = [thinline, thinline4]

R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle 2: '))

def gcd(R,r):
    """Compute the greatest common divisor of a and b"""
    while r > 0:
        R, r = r, R % r
    return R
    
def lcm(R, r):
    """Compute the lowest common multiple of a and b"""
    return R * r / gcd(R, r)


a=0
stylecount = 0
number = 0

def step():
    global a
    global stylecount
    if a < (2*pi*lcm(R,r))/R:
        oldxpen = (R-r)*cos(a) + r*1*cos(((R/r)-1)*a)+250
        oldypen = (R-r)*sin(a) - r*1*sin(((R/r)-1)*a)+240
        a=a+0.2
        xpen = (R-r)*cos(a) + r*1*cos(((R/r)-1)*a)+250
        ypen = (R-r)*sin(a) - r*1*sin(((R/r)-1)*a)+240
        stylecount += 1
        number == floor(stylecount/5)
        asset2 = LineSegment((oldxpen,oldypen), (xpen,ypen), style = listc[number], positioning="physical")
        if number > len(listc):
            number = number - 1
            

        
        # asset = CircleAsset(.5, thinline, black)
         #print("new: ", xpen, ypen)
        
         #print("old: ", oldxpen, oldypen)
        #Sprite(asset, (xpen,ypen))
#rainbow spirograph
# go through once, then delete and add 2 shorter lines, again and again 


    
myapp = App()
myapp.run(step)