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

class Pongblock1(Sprite):
    black = Color(0x000000, 1.0)
    thinline= LineStyle(1, black)
    rectangle=RectangleAsset(400, 100, thinline, black)
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "w", self.up)
        ponggame.listenKeyEvent("keydown","s",self.down)
    def up(self, event):
        self.vy -=2
    def down(self, event):
        self.vy +=2

class Pongblock2(Pongblock1):
    print("kyle")
class pongball(Sprite):
     print("kyle")

class ponggame(App):
     print("kyle")
app=ponggame(0,0)
app.run()