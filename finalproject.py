"""
Finalproject.py
Author: Sam Pych
Credit:
Assignment: Create a pong game with two movable blocks and the ball either bounces off the wall 
or appears on the other side.
optional: keep score
bounde=self.collidingWithSprites(Pongblock1)
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Pongblock(Sprite):
    black = Color(0x000000, 1.0)
    thinline= LineStyle(1, black)
    rectangle_asset=RectangleAsset(50, 200, thinline, black)
    rectangle = Sprite(rectangle_asset, (60,60))
    rectangle1 = Sprite(rectangle_asset, (1400,60))
    def __init__(self, position):
        self.vx = 1
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "w", self.up)
        ponggame.listenKeyEvent("keydown","s",self.down)
    def up(self, event):
        self.vy -= 2
    def down(self, event):
        self.vy +=2
        
class Pongblock1(Pongblock):
    print("kyle")
class Pongblock2(Pongblock):
    print("kyle")
class pongball(Sprite):
     print("kyle")

class ponggame(App):
    def __init__(self , width, height):
        super().__init__(width, height)
        Pongblock1((10,10))
        
        Pongblock2((350,250))
        
app=ponggame(0,0)
app.run()