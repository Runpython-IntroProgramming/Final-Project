# Andy Kotz final project: graphing calculator with regressions

from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset
from math import sin, cos, radians

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
purple = Color(0x9B30FF, 1.0)

thinline = LineStyle(0.5, black)
mycircle = CircleAsset(5, thinline, blue)
mycircle2 = CircleAsset(5, thinline, red)
mycircle3 = CircleAsset(5, thinline, purple)
xcoordinates = range(100, 600, 1)
xcoordinates1 = range(100, 600, 1)
xcoordinates2 = range(100, 600, 1)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (100+100*cos(radians(x)), 100+100*sin(radians(x)) + 400)) for x in xcoordinates]
sprites = [Sprite(mycircle2, (x, 100+100*cos(radians(x)) + 100)) for x in xcoordinates1]
sprites = [Sprite(mycircle3, (x, 400+100*sin(radians(x)) + 100)) for x in xcoordinates2]

myapp = App()
myapp.run()
