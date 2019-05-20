# Rain's final project
# Sources:
# 1. https://math.stackexchange.com/questions/823578/how-do-i-calculate-the-perodicity-of-a-spirograph-hypotrochoid
# 2. https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3

from math import sin, cos, pi
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from ggame.line import LineSegment

black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)

R = float(input('Radius of circle 1: '))
r = float(input('Radius of circle 2: '))

R1 = 2*R*pi 
r1 = 2*r*pi

def gcd(R1,r1):
    """Compute the greatest common divisor of a and b"""
    while r1 > 0:
        R1, r1 = r1, R1 % r1
    return R1
    
def lcm(R1, r1):
    """Compute the lowest common multiple of a and b"""
    return R1 * r1 / gcd(R1, r1)


a=0

def step():
    global a
    if a < lcm(R1,r1):
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
# spirograph repeats when a hits the lcm of both radii
# style; line style
#rainbow spirograph
# go through once, then delete and add 2 shorter lines, again and again 


    
myapp = App()
myapp.run(step)