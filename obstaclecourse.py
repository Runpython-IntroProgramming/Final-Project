from ggame import App, Sprite, ImageAsset, Frame, CircleAsset
from ggame import SoundAsset, Color, LineStyle, TextAsset
import math
from time import time
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 700


myapp = App()

print('Hello everybody, Here is my obstacle course game!!')
print('Use the key W to go forward and use A and D to turn left and right')
print('Dodge the obstacles and collide with the finish line to win!')

class SpaceShip(Sprite):
 
    asset = ImageAsset("images/four_spaceship_by_albertov_with_thrust.png", 
        Frame(227,0,292-227,125), 4, 'vertical')

    def __init__(self, position):
        super().__init__(SpaceShip.asset, position)
        self.vx = 1
        self.vy = 1
        self.vr = 0.01
        self.thrust = 0
        self.thrustframe = 1
        Obstacle.listenKeyEvent("keydown", "w", self.thrustOn)
        Obstacle.listenKeyEvent("keyup", "w", self.thrustOff)
        Obstacle.listenKeyEvent("keydown", "a", self.right)
        Obstacle.listenKeyEvent("keyup", "a", self.stop)
        Obstacle.listenKeyEvent("keydown", "d", self.left)
        Obstacle.listenKeyEvent("keyup", "d", self.stop)
        self.fxcenter = self.fycenter = 0.5
        
        
    def step(self):
        self.x += self.vx
        self.y += self.vy
        self.rotation += self.vr
        
        if self.thrust == 1:
            self.setImage(self.thrustframe)
            self.thrustframe += 0.8
            self.vx += 0.03*math.cos(self.rotation+1/2*math.pi)
            self.vy += 0.03*math.sin(self.rotation-1/2*math.pi)
            if self.thrustframe == 4:
                self.thrustframe = 1
            else:
                self.setImage(3.9)
                nba=self.collidingWithSprites(finish)
                if nba:
                    print('You Win, Press Enter for Next Level')
            
            
            self.setImage(3.9)
        lol=self.collidingWithSprites(obstacle)
        if lol:
            self.explode(self)
            print('GG You Lost')
            

    def thrustOn(self, event):
        self.thrust = 1

    def thrustOff(self, event):
        self.thrust = 0

    def up(self, event):
        self.vy=1 
    def down(self, event):
        self.vy=-1
    def right(self, event):
        self.vr = .1
    def left(self, event):
        self.vr = -.1
    def stop(self, event):
        self.vr=0

    def explode(self, event):
        self.visible = False
        self.vx=0
        self.vy=0
        explosionn(self.position)
    def Win(self, event):
        self.visible = false
        self.vx=0
        self.vy=0
        explosionn(self.position)
        
        
class explosionn(Sprite):
    
    asset = ImageAsset("images/explosion1.png", Frame(0,0,128,128), 10)
   
    def __init__(self, position):
        super().__init__(explosionn.asset, position)
        self.image = 0
        self.center = (0.5, 0.5)
        
        
    def step(self):
        self.setImage(self.image//2)
        self.image = self.image + 1
        if self.image == 10:
            self.destroy()
    
class Obstacle(App):
   
    def __init__(self, width, height):
        super().__init__(width, height)
        asset = ImageAsset("images/beach.jpg")
        Sprite(asset,(10, 10))
        SpaceShip((10,10))
        finish((1014,200))
        obstacle((300,300))
        obstacle((100,550))
        obstacle((300,300))
        obstacle((800,450))
        obstacle((800,20))

        Obstacle.listenKeyEvent("keydown", "space", self.level2)
    
    def step(self):
        for ship in self.getSpritesbyClass(SpaceShip):
            ship.step()
        for explosion in self.getSpritesbyClass(explosionn):
            explosion.step()
    
    def level2(self,event):
        for x in self.getSpritesbyClass(finish):
            x.destroy()
        for x in self.getSpritesbyClass(obstacle):
            x.destroy()
    

class obstacle(Sprite):
    hi = ImageAsset("images/beach-ball-575425_640.png")
    width = 50
    height = 50
    
    def __init__(self, position):
        super().__init__(obstacle.hi, position)
        self.scale = 0.2
class finish(Sprite):
    op = ImageAsset("images/FinishLine.png")
    width = 50
    height = 50
    
    def __init__(self, position):
        super().__init__(finish.op, position)
        self.scale = 0.5




myapp = Obstacle(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
