# Rain's final project
# Sources:
# 1. https://math.stackexchange.com/questions/823578/how-do-i-calculate-the-perodicity-of-a-spirograph-hypotrochoid
# 2. https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3

from math import sin, cos, pi, floor 
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from ggame.line import LineSegment

red = Color(0xF20000, 1.0)
orange = Color(0xF99300, 1.0)
yellow = Color(0xFFE347, 1.0)
green = Color(0x13E105, 1.0)
blue = Color(0x008FDC, 1.0)
purple = Color(0x6F02CF, 1.0)
indigo = Color(0xE212E2, 1.0)
pink = Color(0xFF0C94, 1.0)
barbiepink = Color(0xFF2AA1, 1.0)

thinline = LineStyle(1, red)
thinline1 = LineStyle(1, orange)
thinline2 = LineStyle(1, yellow)
thinline3 = LineStyle(1, green)
thinline4 = LineStyle(1, blue)
thinline5 = LineStyle(1, purple)
thinline6 = LineStyle(1, pink)
thinline7 = LineStyle(1, barbiepink) 

thinline7 = LineStyle(1, indigo)

listr = [thinline, thinline1, thinline2, thinline3, thinline4, thinline5,thinline6]

listd = []
#listd. append(x)

R = float(input('Radius of circle 1 (under 100): '))
r = float(input('Radius of circle 2 (under 70): '))
color = input("If you would like a rainbow spirograph, type 'R'. If you would like to choose your own colors, type 'D'. ")

if color == 'R':
    colorlist = listr
if color == 'D': 
    colorlist = listd
    numcolors = int(input('How many colors would you like? '))
    while numcolors > 0:
        choose = input("For red, type 'r'. \nFor orange, type 'o'. \nFor yellow,, type 'y'.\nFor green, type 'g'. \nFor blue, type 'b'. \nFor purple, type 'p'. \nFor pink, type 'pi'. \n")
        if choose == 'r':
            listd.append(thinline)
        elif choose == 'o':
            listd.append(thinline1)
        elif choose == 'y':
            listd.append(thinline2)
        elif choose == 'g':
            listd.append(thinline3)
        elif choose == 'b':
            listd.append(thinline4)
        elif choose == 'p':
            listd.append(thinline5)
        elif choose == 'pi':
            listd.append(thinline6)
        numcolors -= 1

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
    global number
    if a < (2*pi*lcm(R,r))/R:
        oldxpen = (R-r)*cos(a) + r*3*cos(((R/r)-1)*a)+536
        oldypen = (R-r)*sin(a) - r*3*sin(((R/r)-1)*a)+331.5
        a=a+0.2
        xpen = (R-r)*cos(a) + r*3*cos(((R/r)-1)*a)+536
        ypen = (R-r)*sin(a) - r*3*sin(((R/r)-1)*a)+331.5
        stylecount += 1
        number = floor(stylecount/3)
        asset2 = LineSegment((oldxpen,oldypen), (xpen,ypen), style = colorlist[number], positioning="physical")
        if number == len(colorlist)-1:
            stylecount = 0 

#asset = CircleAsset(.5, thinline, black)
#print("new: ", xpen, ypen)
#print("old: ", oldxpen, oldypen)
#Sprite(asset, (xpen,ypen))
#rainbow spirograph
# go through once, then delete and add 2 shorter lines, again and again 

#55,23
#100, 60
#100,70
#44,12
print(App.width)
print(App.height)

    
myapp = App()
myapp.run(step)