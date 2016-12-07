import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

class ball(Sprite):
    asset=ImageAsset("ball.png")
    


myapp = App()
myapp.run()
    