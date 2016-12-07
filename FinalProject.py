"""
FinalProject.py
Author: Liam S
Credit: 
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Background(Sprite):

    asset = ImageAsset("images/grass_with_blue_sky_by_devrez-d35pm8j.png")
    width = 1032
    height = 774

    def __init__(self, position):
        super().__init__(Background.asset, position)
        self.scale = 1.4

class Ship(Sprite):

    asset = ImageAsset("images/il2m3-bp-fl-am-3view-mongolian.png")

    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.vx = 1
        self.vy = 1
        self.vAddedx = 0
        self.vAddedy = 0
        self.vAddedr = 0
        self.vertThrust = 0
        self.RotThrust = 0
        self.thrustframe = 1
        self.scale = 0.25
        """
        PlaneGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        PlaneGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        PlaneGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        PlaneGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        """
        PlaneGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        PlaneGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        PlaneGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        PlaneGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)

        self.fxcenter = self.fycenter = 0.5
    def step(self):
        """
        if self.sideThrust == 1:
            self.vAddedx += 0.05
        if self.sideThrust == -1:
            self.vAddedx -= 0.05
        if self.sideThrust == 0:
            self.vAddedx += 0
        """
        if self.vertThrust == 1:
            self.vAddedy = 1.3
        if self.vertThrust == -1:
            self.vAddedy = -1.3
        if self.vertThrust == 0:
            self.vAddedy = 0
        if self.RotThrust == 1:
            self.vAddedr = -0.3
        if self.RotThrust == -1:
            self.vAddedr = 0.3
        if self.RotThrust == 0:
            self.vAddedr = 0
        if self.x >= 2000:
            self.x = 10
        if self.x <= 0:
            self.x = 1999
        if self.y <=10:
            self.y = 11 
        self.x += 5
        self.y += self.vAddedy
        self.rotation = self.vAddedr
        if self.y >= 765:
            self.visible = False

    def thrustUp(self, event):
        self.vertThrust = -1
        self.RotThrust = -1

    def thrustDown(self, event):
        self.vertThrust = 1
        self.RotThrust = 1
    
    def thrustDownoff(self, event):
        self.vertThrust = 0
        self.RotThrust = 0
    
    def thrustUpoff(self, event):
        self.vertThrust = 0
        self.RotThrust = 0


class Bomb(Sprite):

    asset = ImageAsset("images/bomb.png")
    width = 2000
    height = 1000

    def __init__(self, position, ship):
        super().__init__(Bomb.asset, position)
        self.scale = 0.04
        self.ship = ship
        self.visible = False
        self.dropped = False
        
        PlaneGame.listenKeyEvent("keydown", "space", self.dropBomb)
        PlaneGame.listenKeyEvent("keyup", "space", self.nodropBomb)
        
    def dropBomb(self, event):
        
    
    def step(self):
        if self.dropped == False:
            self.x = self.ship.x
            self.y = self.ship.y
        if self.y >= 765:
            self.visible = False

    
class PlaneGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Background((0, 0))
        Background((1300, 0))
        s = Ship((400,600))
        Bomb((400,600),s)
                    
    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
        for ship in self.getSpritesbyClass(Bomb):
            ship.step()

            
app = PlaneGame(0,0)
app.run()
    

