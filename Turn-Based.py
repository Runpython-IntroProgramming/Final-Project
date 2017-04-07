from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame, PolygonAsset
from math import pi, cos, sin
SCREEN_WIDTH1 = 640
SCREEN_HEIGHT = 480
black = Color(0, 1)
speed = 10
speed1=4
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)


thinline = LineStyle(1, black)
white = Color(0xffffff, 1)
gray = Color(0x8c8c8c, 1)
noline = LineStyle(0, black)
thinline1 = LineStyle(1, white)
cf = PolygonAsset(((-10,-15),(10,-15),(10,15),(-10,15)), thinline, gray)
class MC(Sprite):
    def __init__(self, position):
        super().__init__(cf, position)
        self.moves = speed1
        SpaceGame.listenKeyEvent("keydown", "d", self.dKey)
        SpaceGame.listenKeyEvent("keydown", "a", self.aKey)
        SpaceGame.listenKeyEvent("keydown", "s", self.sKey)
        SpaceGame.listenKeyEvent("keydown", "w", self.wKey)
        SpaceGame.listenKeyEvent("keydown", "q", self.qKey)
        SpaceGame.listenKeyEvent("keydown", "e", self.eKey)
        
    def dKey(self, event):
        if self.moves > 0:
            self.x += speed*cos(self.rotation)
            self.y -= speed*sin(self.rotation)
            self.moves -=1
    def aKey(self, event):
        if self.moves > 0:
            self.x -= speed*cos(self.rotation)
            self.y += speed*sin(self.rotation)

            self.moves -=1
    def sKey(self, event):
        if self.moves > 0:
            elf.x += speed*cos((pi/2)-self.rotation)
            self.y += speed*sin((pi/2)-self.rotation)
            self.moves -=1
    def wKey(self, event):
        if self.moves > 0:
           self.x -= speed*cos((pi/2)-self.rotation)
           self.y -= speed*sin((pi/2)-self.rotation)
           self.moves-=1
    def qKey(self, event):
        self.rotation+= pi/2
    def eKey(self, event):
        self.rotation-= pi/2
    def step(self):
        global turn
        self.moves = speed1
        
class SpaceGame(App):
    """
    Tutorial4 space game example.
    """
    def __init__(self, width, height):
        super().__init__(width, height)
        black = Color(0, 1)
        noline = LineStyle(0, black)
        bg_asset = RectangleAsset(width, height, noline, white)
        bg = Sprite(bg_asset, (0,0))
        
    def step(self):
        if turn == 1:
            MC1.step()
        
            


myapp = SpaceGame(SCREEN_WIDTH1, SCREEN_HEIGHT)

turn = 0
def turnProgress ():
    global turn
    turn=1
def spaceKey (event):
    turnProgress()
    
myapp.listenKeyEvent('keydown', 'space', spaceKey)
MC1=MC((320,240))


myapp.run()