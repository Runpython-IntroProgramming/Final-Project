# Rain's final project
# Sources:
# 1. https://math.stackexchange.com/questions/823578/how-do-i-calculate-the-perodicity-of-a-spirograph-hypotrochoid
# 2. https://gist.github.com/endolith/114336/eff2dc13535f139d0d6a2db68597fad2826b53c3
# 3. https://htmlcolorcodes.com/

from math import sin, cos, pi, floor 
from ggame import App, Color, LineStyle, Sprite, CircleAsset
from ggame.line import LineSegment

#colors
red = Color(0xFF0000, 1.0)
orange = Color(0xFF8000, 1.0)
yellow = Color(0xFFF700, 1.0)
green = Color(0x00FF1B, 1.0)
blue = Color(0x00CBFF, 1.0)    
purple = Color(0x7B1EFF, 1.0) 
pink = Color(0xFB7CB0 , 1.0)             
hotpink = Color(0xFF00FB, 1.0)
neongreen = Color(0x34FF03, 1.0)
cyanide = Color(0x00FFFF, 1.0)
jade = Color(0x0D8D6C,1.0)
orangecream = Color(0xF76100, 1.0)
apricot = Color(0xFFCD12, 1.0)
icedmint = Color(0x84FEC7, 1.0)

#user input of R, r, line thicknessm and color choice
R = float(input('Radius of circle 1 (under 200): '))               
r = float(input('Radius of circle 2 (under 50): '))
line = input("Would you like thick or thin lines? Type 'T' for thick and 't' for thin. ")
color = input("If you would like a rainbow spirograph, type 'R'. If you would like Rain's special assortment of colors, type 'S'. If you would like to choose your own colors, type 'D'. ")

if line == 'T':
    linethickness = 5
if line == 't':
    linethickness = 1
    
#lines
thinline = LineStyle(linethickness, red)
thinline1 = LineStyle(linethickness, orange)
thinline2 = LineStyle(linethickness, yellow)
thinline3 = LineStyle(linethickness, green)
thinline4 = LineStyle(linethickness, blue)
thinline5 = LineStyle(linethickness, purple)
thinline6 = LineStyle(linethickness, pink) 
thinline7 = LineStyle(linethickness, hotpink)            
thinline8 = LineStyle(linethickness, neongreen) 
thinline9 = LineStyle(linethickness, cyanide) 
thinline10 = LineStyle(linethickness, jade) 
thinline11 = LineStyle(linethickness, orangecream) 
thinline12= LineStyle(linethickness, apricot) 
thinline13= LineStyle(linethickness, icedmint) 

#lists of colors
listr = [thinline, thinline1, thinline2, thinline3, thinline4, thinline5, thinline6]
listS = [thinline10, thinline11, thinline12, thinline13]                                  
listd = []

#code creating the color(s) of the spirograph
if color == 'R':                 
    colorlist = listr
if color == 'S':              
    colorlist = listS
if color == 'D': 
    colorlist = listd
    numcolors = int(input('How many colors would you like (total of 10 options)? '))
    while numcolors > 0:
        choose = input("For red, type 'r'. \nFor orange, type 'o'. \nFor yellow,, type 'y'.\nFor green, type 'g'. \nFor blue, type 'b'. \nFor purple, type 'p'. \nFor pink, type 'pi'. \nFor hot pink, type 'hp'. \nFor neon green, type 'n'. \nFor cyan-ide, type 'c'. \n")
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
        elif choose == 'hp':
            listd.append(thinline7)
        elif choose == 'n':
            listd.append(thinline8)
        elif choose == 'c':
            listd.append(thinline9)
        numcolors -= 1

#gcd and lcm of R and r
def gcd(R,r):
    """Compute the greatest common divisor of a and b"""        
    while r > 0:
        R, r = r, R % r                  
    return R                                    
    
def lcm(R, r):
    """Compute the lowest common multiple of a and b"""
    return R * r / gcd(R, r)

#set all variables to 0 before step function
a=0
stylecount = 0             
number = 0

#step function, creates the spirograph
def step():
    global a
    global stylecount                                          # oldxpen and oldypen --> first x and y values
    global number                                              # xpen and ypen --> x and y values after change in a
    if a < (2*pi*lcm(R,r))/R:                                  # R-r --> radius of circle inside the big circle, has center point of big circle, includes the radius of the little circle 
        oldxpen = (R-r)*cos(a) + r*3*cos(((R/r)-1)*a)+536      # (R-r)*cos(a) --> x-value for center point of little circle
        oldypen = (R-r)*sin(a) - r*3*sin(((R/r)-1)*a)+331.5    # (R-r)*cos(a) --> y-value for center point of little circle
        a=a+0.075                                              # r*3*cos(((R/r)-1)*a) --> x-value distance from the circle described above to the pen
        xpen = (R-r)*cos(a) + r*3*cos(((R/r)-1)*a)+536         # r*3*cos(((R/r)-1)*a) --> y-value distance from the circle described above to the pen
        ypen = (R-r)*sin(a) - r*3*sin(((R/r)-1)*a)+331.5       # the 3 enlarges the spirograph by 3, can be changed to any #
        stylecount += 1
        number = floor(stylecount/3)
        asset = LineSegment((oldxpen,oldypen), (xpen,ypen), style = colorlist[number], positioning="physical")
        if number == len(colorlist)-1:
            stylecount = 0 

#EXTRA FUN:
#asset = CircleAsset(.5, thinline, black)
#lavender = Color(0xCF94F3, 1.0)
#print("new: ", xpen, ypen)
#print("old: ", oldxpen, oldypen)
#Sprite(asset, (xpen,ypen))
#print(App.width)
#print(App.height)
#go through once, then delete and add 2 shorter lines, again and again 
#55,23
#100, 60
#100,70
#44,12
#98,12
#89,49
#150, 47.6
#151,75
#198,40 rainbow, 0.075 

#PRESENTATION:
#150,68 rainbow, thin, 0.075
#180,46 special, thin, 0.075
#198,40 rainbow, thick, 0.2

myapp = App()
myapp.run(step)