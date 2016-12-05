# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset
from ggame import CircleAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)
thinline = LineStyle(0, black)
yaxis = RectangleAsset(1, 1000, thinline, black)
xaxis = RectangleAsset(1900, 1, thinline, black)
xaxisrulings = RectangleAsset(1, 7, thinline, black)
yaxisrulings = RectangleAsset(7, 1, thinline, black)
thinline = LineStyle(0, black)
mycircle = CircleAsset(3, thinline, blue)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (950, 0))
yaxisrulingsprites = [Sprite(yaxisrulings, (947.5, y*20)) for y in range(-100, 100, 1)]
xaxisrulingsprites = [Sprite(xaxisrulings, (x*20+10, 497)) for x in range(-150, 150, 1)]

linetypelist = input("linear, quadratic, cubic (l, q, c). Separate by commas: ")
linetypelist = linetypelist.split(",")
for linetype in linetypelist:
    if linetype == "l":
        m = float(input("m: "))
        b = float(input("b: "))
    if linetype == "q":
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    xcoordinates = range(-900, 900, 1)

    if linetype == "l":
        for x in xcoordinates:
            sprites = Sprite(mycircle, (20*x+950, 20*((-m)*x-b)+500))
    if linetype == "q":
        sprites = [Sprite(mycircle, (x+950, -a*x**2-b*x-c+500)) for x in xcoordinates]



myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
