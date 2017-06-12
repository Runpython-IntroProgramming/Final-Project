"""
Finalproject.py
Author: Sam Pych
Credit: Thomas Kyle Postans, Hagin
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
    #rectangle1 = Sprite(rectangle_asset, (1100,250))
    def __init__(self, position):
        super().__init__(Pongblock1.rectangle_asset, position)
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "up arrow", self.up)
        ponggame.listenKeyEvent("keydown","left arrow",self.left)
        ponggame.listenKeyEvent("keydown","down arrow",self.down)
        ponggame.listenKeyEvent("keydown","right arrow",self.right)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.y += self.vy
        #self.y += self.vy
        if self.y >400:
            self.y=399
        if self.y <-1:
            self.y=0
    def up(self, event):
        self.vy -=2
    def down(self, event):
        self.vy +=2
    def left(self, event):
        self.vx -=2
    def right(self, event):
        self.vx +=2
    
        
class Pongblock1(Sprite):
    black = Color(0x000000, 1.0)
    thinline= LineStyle(1, black)
    rectangle_asset=RectangleAsset(50, 200, thinline, black)
    #rectangle1 = Sprite(rectangle_asset, (1100,250))
    def __init__(self, position):
        super().__init__(Pongblock1.rectangle_asset, position)
        self.vy = 1
        ponggame.listenKeyEvent("keydown", "w", self.up)
        ponggame.listenKeyEvent("keydown","a",self.left)
        ponggame.listenKeyEvent("keydown","s",self.down)
        ponggame.listenKeyEvent("keydown","d",self.right)
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        self.y += self.vy
        #self.y += self.vy
        if self.y >400:
            self.y=399
        if self.y <-1:
            self.y=0
    def up(self, event):
        self.vy -=2
    def down(self, event):
        self.vy +=2
    def left(self, event):
        self.vx -=2
    def right(self, event):
        self.vx +=2
    
class pongball(Sprite):
    red = Color(0xff0000, 1.0)
    thinline= LineStyle(1, red)
    circle_asset=CircleAsset(25, thinline, red)
    #circle1 = Sprite(circle_asset, (600,300))
    circle=CircleAsset(1500, thinline, red)
    
    def __init__(self, position):
        super().__init__(pongball.circle_asset, position)
        self.vx = 1
        self.vy = 1
        
    def step(self):
        if self.visible:
            collides = self.collidingWithSprites(Scoreline)
            collides = self.collidingWithSprites(Scoreline2)
            if len(collides):
                if collides[0].visible:
                    collides[0].explode()
                    self.explode()
        self.x += self.vx
        
class Scoreline(Sprite):
    blue = Color(0x0000ff, 1.0)
    thinline= LineStyle(1, blue)
    rectangle_asset=RectangleAsset(10, 1200, thinline, blue)
    rectangle = Sprite(rectangle_asset, (00,-600))
class Scoreline2(Sprite):
    blue = Color(0x0000ff, 1.0)
    thinline= LineStyle(1, blue)
    rectangle_asset=RectangleAsset(10, 1200, thinline, blue)
    rectangle = Sprite(rectangle_asset, (1200,-600))
class Scoreboard:
    print("kyle")
class ponggame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Pongblock1((100,10))
        
        Pongblock((1100,250))
        
        pongball((600,400))
        
    def step(self):
        for x in self.getSpritesbyClass(Pongblock1):
            x.step()
        for x in self.getSpritesbyClass(Pongblock):
            x.step()
        for x in self.getSpritesbyClass(pongball):
            x.step()
app = ponggame(0,0)
app.run()