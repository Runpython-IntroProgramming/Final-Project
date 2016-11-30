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

    asset = ImageAsset("images/iStock_000005669855Medium.jpg")
    width = 1698
    height = 1131

    def __init__(self, position):
        super().__init__(Background.asset, position)
        self.scale = 0.8

class Ship(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,230,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.vx = 1
        self.vy = 1
        self.vAddedx = 0
        self.vAddedy = 0
        self.vAddedr = 0
        self.sideThrust = 0
        self.vertThrust = 0
        self.RotThrust = 0
        self.thrust = 0
        self.thrustframe = 1
        PlaneGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        PlaneGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        PlaneGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        PlaneGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        
        PlaneGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        PlaneGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        PlaneGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        PlaneGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)
        
        
        PlaneGame.listenKeyEvent("keydown", "i", self.thrustCounterClock)
        PlaneGame.listenKeyEvent("keyup", "p", self.thrustClockoff)
        PlaneGame.listenKeyEvent("keyup", "i", self.thrustCounterClockoff)
        PlaneGame.listenKeyEvent("keydown", "p", self.thrustClock)
        
        self.fxcenter = self.fycenter = 0.5
    def step(self):
        if self.sideThrust == 1:
            self.vAddedx += 0.05
        if self.sideThrust == -1:
            self.vAddedx -= 0.05
        if self.sideThrust == 0:
            self.vAddedx += 0
        if self.vertThrust == 1:
            self.vAddedy += 0.05
        if self.vertThrust == -1:
            self.vAddedy -= 0.05
        if self.vertThrust == 0:
            self.vAddedy += 0
        if self.RotThrust == 1:
            self.vAddedr = -0.03
        if self.RotThrust == -1:
            self.vAddedr = 0.03
        if self.RotThrust == 0:
            self.vAddedr = 0
        if self.x >= 2000:
            self.x = 10
        if self.x <= 0:
            self.x = 1999
        if self.y <=10:
            self.vAddedy = -self.vAddedy 
        self.x += self.vAddedx
        self.y += self.vAddedy
        self.rotation += self.vAddedr
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
        else:
            self.setImage(0)
    def thrustOff(self, event):
        self.thrust = 0
        
    def thrustLeft(self, event):
        self.sideThrust = -1
        self.thrust = 1

    def thrustRight(self, event):
        self.sideThrust = 1
        self.thrust = 1
    
    def thrustRightoff(self, event):
        self.sideThrust = 0
        self.thrust = 0
    
    def thrustLeftoff(self, event):
        self.sideThrust = 0
        self.thrust = 0
    
    def thrustUp(self, event):
        self.vertThrust = -1
        self.thrust = 1

    def thrustDown(self, event):
        self.vertThrust = 1
        self.thrust = 1
    
    def thrustDownoff(self, event):
        self.vertThrust = 0
        self.thrust = 0
    
    def thrustUpoff(self, event):
        self.vertThrust = 0
        self.thrust = 0

    def thrustCounterClock(self, event):
        self.RotThrust = -1
        self.thrust = 1

    def thrustClock(self, event):
        self.RotThrust = 1
        self.thrust = 1
    
    def thrustClockoff(self, event):
        self.RotThrust = 0
        self.thrust = 0
    
    def thrustCounterClockoff(self, event):
        self.RotThrust = 0
        self.thrust = 0

class PlaneGame(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        Background((0, 0))
        Ship((400,600))
                    
    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()

            
app = PlaneGame(0,0)
app.run()
    

