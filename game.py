from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500

class Field(Sprite):
    field=ImageAsset("images/field.jpg")

    def __init__(self, position):
         super().__init__(Field.field, position)
         self.vx=1
         self.vy=1
         self.vr=0

class AOA():
    def __init__(self, r):
        self.rotation = r
    def anglex(self):
        return (-1 * math.cos(self.rotation))
    def angley(self):
        return (-1 * math.sin(self.rotation))
        
class Plane(Sprite):
    airplane = ImageAsset("images/28293b2fe5801e03f1f70ed61c8397f6_airplane-clipart-transparent-airplane-clipart-transparent-background_2400-1009.png")
    def __init__(self, position):
        super().__init__(Plane.airplane, position)
        self.vx = 0
        self.vy = 0
        self.vr = 0
        self.scale = 0.1
        Game.listenKeyEvent("keydown", "d", self.Forward)
        Game.listenKeyEvent("keydown", "a", self.Slow)
        Game.listenKeyEvent("keydown", "left arrow", self.Up)
        Game.listenKeyEvent("keydown", "right arrow", self.Down)
        Game.listenKeyEvent("keyup", "right arrow", self.Stop)
        Game.listenKeyEvent("keyup", "left arrow", self.Stop)
        Game.listenKeyEvent("keydown", "e", self.Print)
        self.fxcenter = self.fycenter = 0.5
        
        
    def Forward(self, event):
        self.vx += 0.6
    def Slow(self, event):
        self.vx -= 0.6
    def Up(self, event):
        self.vr += 0.1
        #self.vx=angle.anglex()
        #self.vy=angle.angley()
    def Down(self, event):
        self.vr -= 0.1
        #self.vx=angle.anglex()
        #self.vy=angle.angley()
    def Stop(self, event):
        self.vr=0
    def Print(self, event):
        print(self.rotation)
    
    def step(self):
        #while self.vx >= 0:
        #self.vx -= 0.4
        #while self.vy >= 0:
        #self.vy -= 0.4
        self.rotation += self.vr
        #angle=AOA(self.rotation)
        self.y += self.vy
        self.x += self.vx
        
    
class Game(App):
    def __init__(self, width, height):
        super().__init__(width, height)
        """
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
        bg = Sprite(bg_asset, (0,0))
        """
        Field((0,0))
        Plane((0,500))
        
    def step(self):
        for airplane in self.getSpritesbyClass(Plane):
            airplane.step()
            
myapp = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()
