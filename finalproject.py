"""
Finalproject.py
Author: Sam Pych
Credit:
Assignment: Create a pong game with two movable blocks and the ball either bounces off the wall 
or appears on the other side.
optional: keep score
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

class Pongblock1(Sprite):
    asset=ImageAsset("",Frame(227,0,292-227,125), 4, 'vertical'))
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "w", self.up)
        ponggame.listenKeyEvent("keydown","s",self.down)
        

class Pongblock2(Sprite):
    asset=ImageAsset(""Frame(227,0,292-227,125), 4, 'vertical'))
    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "w", self.up)
        ponggame.listenKeyEvent("keydown","s",self.down)

class pongball(Sprite):


class ponggame(Sprite):
    
app=ponggame(0,0)
app.run()