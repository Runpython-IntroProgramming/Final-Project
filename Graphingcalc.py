# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite, RectangleAsset
from ggame import CircleAsset
from math import sin, cos, radians

SCREEN_WIDTH = 1700
SCREEN_HEIGHT = 1000

m = int(input("m: "))
b = int(input("b: "))

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)
thinline = LineStyle(0, black)
yaxis = RectangleAsset(1, 1000, thinline, black)
xaxis = RectangleAsset(1700, 1, thinline, black)
thinline = LineStyle(0.5, black)
mycircle = CircleAsset(1, thinline, blue)
Sprite (xaxis, (0, 500))
Sprite (yaxis, (850, 0))

xcoordinates = range(-1000, 1000, 2)


#sprites = [Sprite(mycircle, (100+100*cos(radians(x)), 100+100*sin(radians(x)) + 400)) for x in xcoordinates]
#sprites = [Sprite(mycircle, (x, 100+100*cos(radians(x)) + 100)) for x in xcoordinates]
sprites = [Sprite(mycircle, (x+850, m*x+b+500)) for x in xcoordinates]

myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
