import ggame
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from random import random
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 910
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

class Ball(Sprite):
    asset=ImageAsset("ball.png")
    def __init__(self, position):
        super().__init__(Ball.asset, position)
        Ball((100,100))
    


myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
    