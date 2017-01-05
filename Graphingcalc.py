# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset, TextAsset
from ggame import CircleAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

def correlation(xlistpts,ylistpts):
    N = len(xlistpts)
    corgofor = 0
    Exylist = []
    while corgofor <= len(xlistpts)-1:
        jum = xlistpts[corgofor]*ylistpts[corgofor]
        Exylist.append(jum)
        corgofor += 1
    Exy = sum(Exylist)
    Ex = sum(xlistpts)
    Ey = sum(ylistpts)
    Ex2list = []
    Ey2list = []
    for j in xlistpts:
        jummy = j**2
        Ex2list.append(jummy)
    for i in ylistpts:
        jumby = i**2
        Ey2list.append(jumby)
    Ex2 = sum(Ex2list)
    Ey2 = sum(Ey2list)
    numerator = (N*Exy)-(Ex*Ey)
    denominator = (((N*Ex2)-(Ex)**2)*((N*Ey2)-(Ey)**2))**0.5
    r = numerator/denominator
    return (r)

coords = None
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)
grey = Color(0xd3d3d3, 0.7)
thinline = LineStyle(0, black)
yaxis = RectangleAsset(1, 1000, thinline, black)
xaxis = RectangleAsset(1900, 1, thinline, black)
ycursor =  RectangleAsset(1, 1000, thinline, grey)
xcursor = RectangleAsset(1900, 1, thinline, grey)
class Xcursorclass(Sprite):
    def __init__(self, position):
        super().__init__(xcursor, position)
class Ycursorclass(Sprite):
    def __init__(self, position):
        super().__init__(ycursor, position)
xcurse = Xcursorclass((0,0))
ycurse = Ycursorclass((0,0))
xaxisrulings = RectangleAsset(1, 7, thinline, black)
yaxisrulings = RectangleAsset(7, 1, thinline, black)
thinline = LineStyle(0, black)
circle = CircleAsset(3, thinline, blue)
circlebig = CircleAsset(6, thinline, red)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (950, 0))
yaxisrulingsprites = [Sprite(yaxisrulings, (947.5, y*20)) for y in range(-100, 100, 1)]
xaxisrulingsprites = [Sprite(xaxisrulings, (x*20+10, 497)) for x in range(-150, 150, 1)]

xcoordinates2 = range(-1500, 1500, 1)
xcoordinates = []
for x in xcoordinates2:
    x = x/32
    xcoordinates.append(x)

linetypelist = input("choose function, plot (f,p). Separate by commas: ")
linetypelist = linetypelist.split(",")
for linetype in linetypelist:
    if linetype == "f":
        function = input("y=")
        for x in xcoordinates:
            yval = (-20*(eval(function))+500)
            if yval >= 0 and yval <= 1000:
                Sprite (circle, ((20*x+950), yval))
    if linetype == "p":
        again = True
        ylistpts=[]
        xlistpts=[]
        while again == True:
            point = input("input point x,y. press q to quit, r to regress: ")
            if point == "q" or point == "r":
                again = False
            if again == True:
                point = point.split(",")
                xlistpts.append(float(point[0]))
                ylistpts.append(float(point[1]))
            if point == "r":
                xlistmean = (sum(xlistpts))/len(xlistpts)
                ylistmean = (sum(ylistpts))/len(ylistpts)
                xmeanlist = []
                ymeanlist = []
                for i in xlistpts:
                    x = i-xlistmean
                    x = x**2
                    xmeanlist.append(x)
                for i in ylistpts:
                    y = i-ylistmean
                    y = y**2
                    ymeanlist.append(y)
                sdx = (sum(xmeanlist)/len(xmeanlist))**0.5
                sdy = (sum(ymeanlist)/len(ymeanlist))**0.5
                rval = correlation(xlistpts, ylistpts)
                regreslope = rval*(sdy/sdx)
                regreintercept = ylistmean - (regreslope*xlistmean)
                print ("Regression: y="+str(regreslope)+"x+"+str(regreintercept)+". r = " + str(rval))
                for x in xcoordinates:
                    yval = (-20*(regreslope*x+regreintercept)+500)
                    if yval >= 0 and yval <= 1000:
                        Sprite (circle, ((20*x+950), yval))
                goforh = 0
                while goforh <= len(xlistpts)-1:
                    Sprite(circlebig, (20*float(xlistpts[goforh])+950, -20*float(ylistpts[goforh])+500))

def mousePosition(event):
    global text
    global coords
    if coords != None:
        coords.destroy()
    xcurse.y = event.y-7
    ycurse.x = event.x-9
    text = TextAsset("(" + str(round((event.x-959)/20)) + "," + str(round((-(event.y-507))/20)) + ")", style = '10pt Arial')
    coords = Sprite(text, (event.x-7, event.y-22))
    

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
myapp.listenMouseEvent('mousemove', mousePosition)
