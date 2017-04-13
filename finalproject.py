
from ggame import App, RectangleAsset, ImageAsset, Sprite, LineStyle, Color, Frame

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
black = Color(0, 1)
lgreen = Color(0xd9ffcc, 1.0)
dgreen = Color(0x006600, 1.0)
purp = Color(0x9900cc, 1.0)
blue = Color(0x3399ff,1.0)
gold = Color(0xcc9900, 1.0)
noline = LineStyle(0, black)
topr = RectangleAsset (1080, 20, noline, dgreen) 
botr = RectangleAsset (1080, 20, noline, dgreen) 
sider = RectangleAsset (20, 720, noline, dgreen) 
player = RectangleAsset (20, 50, noline, purp)
prize = RectangleAsset (35, 15, noline, gold)
vy=0
vx=0
ti=0

class dk(App):
    def __init__(self, width, height):
            super().__init__(width, height)
            bg_asset = RectangleAsset(width, height, noline, lgreen)
            bg = Sprite(bg_asset, (0,0))
    def step (self):
        playe.step()
    

class top(Sprite):
    def __init__(self,position):
        super().__init__(topr, position)

class bot(Sprite):
    def __init__(self,position):
        super().__init__(botr, position)

class side(Sprite):
    def __init__(self,position):
        super().__init__(sider, position)
        
class win(Sprite):
    def __init__(self,position):
        super().__init__(prize, position)
        
class play(Sprite):
    def __init__(self, position, vx, vy, ti):
        super().__init__(player, position)
        dk.listenKeyEvent('keydown', 'left arrow', self.lup)
        dk.listenKeyEvent('keydown', 'right arrow', self.rup)
        dk.listenKeyEvent('keydown', 'up arrow', self.uup)
        self.vx=vx
        self.vy=vy
        self.ti=ti
    def step(self):
        self.ti=self.ti+0.02
        self.vy =self.ti*self.vy
        self.y=self.y+self.vy
        self.x=self.x+self.vx
        on = self.collidingWithSprites(top)
        if len(on) > 0:
            ti = 0
            self.vy = 0
        under = self.collidingWithSprites(bot)
        if len(under) > 0:
            self.vy=-self.vy
        csides = self.collidingWithSprites(side)
        if len(csides) > 0:
            self.vx=-self.vx
    def rup(self, event):
        if self.vx<5:
            self.vx+=1
    def lup(self, event):
        if self.vx>-5:
            self.vx-=1
    def uup(self, event):
        self.vy-=2
        
        
        

myapp = dk(SCREEN_WIDTH, SCREEN_HEIGHT)

top ((0, 710))
bot ((0, -10))
side ((-10, 0))
side ((1070, 0))

top ((500, 580))
bot ((500, 590))
top ((-800, 580))
bot ((-800, 590))

top ((800, 450))
bot ((800, 460))
top ((-400, 450))
bot ((-400, 460))

top ((700, 320))
bot ((700, 330))
top ((-500, 320))
bot ((-500, 330))

top ((900, 190))
bot ((900, 200))
top ((-300, 190))
bot ((-300, 200))

playe = play((1000, 640), 0, 0, 0)
prizee = win((300, 175))



    













myapp.run()