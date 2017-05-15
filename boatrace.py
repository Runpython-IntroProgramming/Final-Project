"""
spaceshooter.py
Author: will laycock
Credit: me

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
from math import sin, cos

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class BigExplosion(Sprite):
    
    asset = ImageAsset("images/explosion2.png", Frame(0,0,4800/25,195), 25)
    
    def __init__(self, position):
        super().__init__(BigExplosion.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        
    def step(self):
        self.setImage(self.image//2) 
        self.image = self.image + 1
        if self.image == 50:
            self.destroy()

class Ocean(Sprite):

    asset = ImageAsset("images/toonvectors-83952-140.jpg")

    def __init__(self, position):
        super().__init__(Ocean.asset, position)

class Buoy(Sprite):
    
    asset = ImageAsset("images/0ca8f4b47e5786473f59b66fedf0b96a_float20clipart-lobster-buoy-clip-art_300-267.png")
    
    def __init__(self, position):
        super().__init__(Buoy.asset, position)
        self.mass = 30*1000
        self.scale=0.2
        self.fxcenter = 0.5
        self.fycenter = 0.5
        self.circularCollisionModel()

class Ship(Sprite):
    asset = ImageAsset("images/Rivamare-Birds-eye-view-drawing.png")

    def __init__(self, position):
        super().__init__(Ship.asset, position)
        self.scale=0.05
        self.vx = 1
        self.vy = 1
        self.vr = 0
        self.v = 0
        self.thrust = 0
        self.thrustframe = 1
        self.assignkeys()
        self.initposition = position
        self.fxcenter = self.fycenter = 0.5
    
    def assignkeys(self):
        BoatGame.listenKeyEvent("keydown", "up arrow", self.thrustOn)
        BoatGame.listenKeyEvent("keyup", "up arrow", self.thrustOff)
        BoatGame.listenKeyEvent("keydown", "left arrow", self.turnleft)
        BoatGame.listenKeyEvent("keyup", "left arrow", self.turnoff)
        BoatGame.listenKeyEvent("keydown", "right arrow", self.turnright)
        BoatGame.listenKeyEvent("keyup", "right arrow", self.turnoff)
    
    def step(self):
        vx = cos(self.rotation) * self.v
        vy = -sin(self.rotation) * self.v
        self.x += vx
        self.y += vy
        ki=self.collidingWithSprites(Buoy)
        self.rotation += self.vr
        if self.x > myapp.width:
            self.x = 0
        if self.x < 0:
            self.x = myapp.width
        if self.y > myapp.height:
            self.y = 0
        if self.y < 0:
            self.y = myapp.height
        if len(ki) > 0:
            BigExplosion((self.x,self.y))
            self.visible=False
            self.x = 300
            self.y = 200
            self.v=0
            self.rotation=0
            self.thrust=0
            self.visible=True
        if self.thrust == 0 and self.v >= 0.1:
            self.v -= 0.1
        if self.thrust == 1 and self.v == 0:
            self.v = 1
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 1
            if self.thrustframe == 4:
                self.thrustframe = 1
            if self.v < 12:
                self.v *= 1.1
        else:
            self.setImage(0)
    def thrustOn(self, event):
        self.thrust = 1
        
        
    def thrustOff(self, event):
        self.thrust = 0
    
    def turnleft(self, event):
        self.vr = 0.1
    
    def turnoff(self, event):
        self.vr = 0
        
    def turnright(self, event):
        self.vr = -0.1
        
    def registerKeys(self, keys):
        commands = ["left", "right", "forward", "fire"]
        self.keymap = dict(zip(keys, commands))
        [self.app.listenKeyEvent("keydown", k, self.controldown) for k in keys]
        [self.app.listenKeyEvent("keyup", k, self.controlup) for k in keys]
        
    def controldown(self, event):
        if command == "forward":
                self.thrust = 40.0
                self.imagex = 1 # start the animated rockets
                self.setImage(self.imagex)
    def controlup(self, event):
        command = self.keymap[event.key]
        if command == "forward":
            self.thrust = 0.0
            self.imagex = 0 # stop the animated rockets
            self.setImage(self.imagex)
class Ship2(Ship):
    def assignkeys(self):
        print('A')
        BoatGame.listenKeyEvent("keydown", "space", self.thrustOn)
        BoatGame.listenKeyEvent("keyup", "space", self.thrustOff)
        BoatGame.listenKeyEvent("keydown", "a", self.turnleft)
        BoatGame.listenKeyEvent("keyup", "a", self.turnoff)
        BoatGame.listenKeyEvent("keydown", "d", self.turnright)
        BoatGame.listenKeyEvent("keyup", "d", self.turnoff)


class BoatGame(App):
    def __init__(self, width, height):
        super().__init__()
        ocean = Ocean((0,0))
        ocean.scale = self.width/ocean.width
        self.ss = Ship((300,200))
        self.sv= Ship2((600,200))
        Buoy((self.width/2,self.height/2))
        
    def step(self):
        for ship in self.getSpritesbyClass(Ship):
            ship.step()
        for exp in self.getSpritesbyClass(BigExplosion):
            exp.step()
            


myapp = BoatGame(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
