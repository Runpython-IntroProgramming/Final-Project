"""
FinalProject.py
Author: Liam S
Credit: 
"""
from ggame import App, Sprite, ImageAsset, Frame
from ggame import SoundAsset, Sound, TextAsset, Color
import math
from time import time

class Stars(Sprite):

    asset = ImageAsset("images/starfield.jpg")
    width = 512
    height = 512

    def __init__(self, position):
        super().__init__(Stars.asset, position)

class Moon(Sprite):

    asset = ImageAsset("images/Le_Voyage_dans_la_lune_Transparent.png")
    def __init__(self, position):
        super().__init__(Moon.asset, position)
        self.counter = 0
        self.vx = 0
        self.vy = 0
        self.scale = 0.4
        self.fxcenter = self.fycenter = 0.5
        self.circularCollisionModel()
    def step(self):
        if self.counter >= 0 and self.counter <= 1200:
            self.vx = 1
            self.vy = 0
        if self.counter >= 1200 and self.counter <= 1800:
            self.vx = 0
            self.vy = 1
        if self.counter >= 1800 and self.counter <= 3000:
            self.vx = -1
            self.vy = 0
        if self.counter >= 3000 and self.counter <= 3600:
            self.vx = 0
            self.vy = -1
        if self.counter == 3601:
            self.counter = 0
        self.counter += 1
        
        self.x += self.vx
        self.y += self.vy
class SpaceShip(Sprite):

    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(0,0,230,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
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
        self.circularCollisionModel()
        SpaceGame.listenKeyEvent("keydown", "left arrow", self.thrustLeft)
        SpaceGame.listenKeyEvent("keyup", "right arrow", self.thrustRightoff)
        SpaceGame.listenKeyEvent("keyup", "left arrow", self.thrustLeftoff)
        SpaceGame.listenKeyEvent("keydown", "right arrow", self.thrustRight)
        
        SpaceGame.listenKeyEvent("keydown", "up arrow", self.thrustUp)
        SpaceGame.listenKeyEvent("keyup", "down arrow", self.thrustDownoff)
        SpaceGame.listenKeyEvent("keyup", "up arrow", self.thrustUpoff)
        SpaceGame.listenKeyEvent("keydown", "down arrow", self.thrustDown)
        
        
        SpaceGame.listenKeyEvent("keydown", "i", self.thrustCounterClock)
        SpaceGame.listenKeyEvent("keyup", "p", self.thrustClockoff)
        SpaceGame.listenKeyEvent("keyup", "i", self.thrustCounterClockoff)
        SpaceGame.listenKeyEvent("keydown", "p", self.thrustClock)
        
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
        booming = self.collidingWithSprites(Moon)
        if len(booming) > 0:
            self.visible = False
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
        Ship((400,500))
                    
    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
            
app = PlaneGame(0,0)
app.run()
    

