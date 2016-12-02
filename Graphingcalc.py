# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset
from ggame import CircleAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

linetype = input("linear, quadratic, cubic (l, q, c): ")
if linetype == "l":
    m = float(input("m: "))/100
    b = float(input("b: "))/100
if linetype == "q":
    a = float(input("a: "))/100
    b = float(input("b: "))/100
    c = float(input("c: "))/100

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)
thinline = LineStyle(0, black)
yaxis = RectangleAsset(1, 1000, thinline, black)
xaxis = RectangleAsset(1900, 1, thinline, black)
xaxisrulings = RectangleAsset(1, 5, thinline, black)
yaxisrulings = RectangleAsset(5, 1, thinline, black)
thinline = LineStyle(0.5, black)
mycircle = CircleAsset(2, thinline, blue)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (950, 0))
yaxisrulingsprites = [Sprite(yaxisrulings, (0, y*100)) for y in list(range(-10, 10))]

xcoordinates = range(-600, 600, 1)

if linetype == "l":
    sprites = [Sprite(mycircle, (x+950, (-m)*x-b+500)) for x in xcoordinates]
if linetype == "q":
    sprites = [Sprite(mycircle, (x+950, -a*x**2-b*x-c+500)) for x in xcoordinates]

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
